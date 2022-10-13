#!/usr/bin/env python

"""qc-sim report generator"""

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re
import argparse
import traceback
import sys


def dictify(soup):
    """from nested bullet points to dictionary"""
    result = {}
    for ul in soup.body.find_all("ul"):
        for li in ul.find_all("li"):
            key = next(li.stripped_strings)
            ul = li.find("ul")
            if ul:
                result[key] = []
                for li in ul.find_all("li"):
                    result[key].append(next(li.stripped_strings))
                    for a in li.find_all("a"):
                        result[key][-1] += " " + next(a.stripped_strings)
    # drop invalid keys
    # print(len(result.keys()))
    result.pop("Description: Qinf quantum information and entanglement package")
    result.pop("Yao.jl")
    result.pop("Webpage:")
    # print(len(result.keys()))
    return result


def dataframe(dic):
    """from dictionary to dataframe"""
    df_dict = {}
    for col in [
        "name",
        "cpu",
        "gpu",
        "qpu",
        "qudit",
        "status",
        "lang",
        "webpage",
        "tags",
        "description",
    ]:
        df_dict[col] = []
    for i, name in enumerate(list(dic.keys())[:-1]):
        df_dict["name"].append(name)
        for prop in dic[name]:
            m = re.match("^(Description|Status|Webpage|Repository):? +(.*)", prop)
            if m:
                key = m.group(1).lower().replace("repository", "webpage")
                value = m.group(2).lower() if key == "status" else m.group(2)
                df_dict[key].append(value)
            else:
                print(f"debug: {name}\ndebug: {prop}")
        # empty values for empty columns
        for prop in ["cpu", "gpu", "qpu", "qudit", "lang", "tags"]:
            df_dict[prop].append("")
    # for col in ["name", "description", "webpage", "status"]:
    #    print(f"{col}: {len(df_dict[col])}")
    return pd.DataFrame.from_dict(df_dict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantum simulator report")
    parser.add_argument(
        "--readme", action="store_true", help="create final report as readme"
    )
    args = parser.parse_args()
    # default action
    quantiki_url = "https://www.quantiki.org/wiki/list-qc-simulators"
    try:
        quantiki_page = requests.get(quantiki_url)
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    quantiki_soup = bs(quantiki_page.text, features="lxml")
    quantiki_dict = dictify(quantiki_soup)
    quantiki_df = dataframe(quantiki_dict)
    quantiki_df_nodesc = quantiki_df.drop(columns="description")
    print(f"info: {quantiki_df.shape[0]} qc-sim")
    # select active projects
    quantiki_df_nodesc_active = quantiki_df_nodesc[
        quantiki_df_nodesc["status"].str.contains("active")
    ].reset_index(drop=True)
    print(f"info: {quantiki_df_nodesc_active.shape[0]} active qc-sim")
    quantiki_df_nodesc_active.to_json("quantiki.json", indent=4, orient="records")
    # if final report required
    if args.readme:
        with open("README.md", "w") as fso:
            fso.write("# qc-sim\n")
            with open("toc.md", "r") as fsi:
                fso.write(fsi.read())
            fso.write(f"### From [quantiki]({quantiki_url})\n")
            # legend
            with open("legend.md", "r") as fsi:
                fso.write(fsi.read())
            fso.write("#### Active simulators\n")
            try:
                quantiki_fill_df = pd.read_json("quantiki-fill.json", orient="records")
                df = quantiki_fill_df.drop(columns="status")
                df.to_markdown(fso)
                fso.write("\n#### Active simulators with desired feats\n")
                dff = df[
                    ~df["tags"].str.contains("nebraska")
                    & ~df["tags"].str.contains("proprietary")
                    & ~df["tags"].str.contains("unfit")
                    & ~df["tags"].str.contains("404")
                ].reset_index(drop=True)
                dff.to_markdown(fso)
                fso.write(f"\n### From internet search\n")
                fso.write("#### Simulators with desired feats\n")
                otherwise_df = pd.read_json("otherwise.json", orient="records")
                otherwise_df.to_markdown(fso)
            except Exception:
                traceback.print_exc()
                sys.exit(1)
