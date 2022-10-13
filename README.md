# qc-sim
**Quantum computing simulators report**
* [From quantiki](#From-quantiki)
  * [Active simulators](#Active-simulators)
  * [Active simulators with desired feats](#Active-simulators-with-desired-feats)
* [From internet search](#From-internet-search)
  * [Simulators with desired feats](#Simulators-with-desired-feats)
### From [quantiki](https://www.quantiki.org/wiki/list-qc-simulators)
**Legend**
| symbol | meaning |
| --: | :---|
| x   | hardware support |
| x!   | cluster hardware support |
| >    | forward this support to lower framework |
| <    | backward this support from higher framework |
| nebraska | [unmantained project](https://imgs.xkcd.com/comics/dependency.png) |
| unfit | not our purpose |
| 404 | not found, link broken |
#### Active simulators
|    | name                                                                                                                                    | cpu   | gpu   | qpu   | qudit   | lang        | webpage                                                                                   | tags                                                     |
|---:|:----------------------------------------------------------------------------------------------------------------------------------------|:------|:------|:------|:--------|:------------|:------------------------------------------------------------------------------------------|:---------------------------------------------------------|
|  0 | Intel Quantum Simulator (IQS, former qHiPSTER)                                                                                          | x!    |       |       |         | c++/python  | https://github.com/iqusoft/intel-qs https://arxiv.org/abs/2001.10554                      | intel,mpi,mkl                                            |
|  1 | staq                                                                                                                                    | >     | >     | >     |         | c++/python  | https://github.com/softwareqinc/staq                                                      | openqasm,device_mapper,transpiler:quil,projectq,q#,circq |
|  2 | QuEST                                                                                                                                   | x!    | x!    | >     |         | c++/c       | https://quest.qtechtheory.org https://arxiv.org/abs/1802.08032                            | cuda,openmp,mpi,qasm                                     |
|  3 | Scaffold/ScaffCC                                                                                                                        | >     |       | >     |         | c++/c       | https://www.cs.princeton.edu/research/techreps/TR-934-12 https://github.com/epiqc/ScaffCC | scaffold_dsl,compiler,qasm                               |
|  4 | Qrack                                                                                                                                   | x     | x     |       |         | c++/python  | https://vm6502q.readthedocs.io                                                            | opencl,s/qiskit-aer/qrack,s/projectq/qrack               |
|  5 | QX Simulator                                                                                                                            |       |       |       |         |             | http://quantum-studio.net/                                                                | nebraska                                                 |
|  6 | Quantum++                                                                                                                               | x     |       |       |         | c++/python  | https://github.com/softwareQinc/qpp                                                       | openmp,eign3                                             |
|  7 | Eqcs                                                                                                                                    |       |       |       |         |             | http://home.snafu.de/pbelkner/eqcs/                                                       | nebraska                                                 |
|  8 | qsims                                                                                                                                   |       |       |       |         |             | http://qsims.sourceforge.net/                                                             | nebraska                                                 |
|  9 | Quantum Construct (qC++)                                                                                                                |       |       |       |         |             | http://sourceforge.net/projects/qcplusplus/                                               | nebraska                                                 |
| 10 | Quantum Network Computing                                                                                                               |       |       |       |         |             | http://sourceforge.net/projects/qnc/                                                      | nebraska                                                 |
| 11 | Qubiter                                                                                                                                 |       |       |       |         |             | https://github.com/artiste-qb-net/qubiter                                                 | nebraska                                                 |
| 12 | QuCoSi                                                                                                                                  |       |       |       |         |             | http://qucosi.sourceforge.net/                                                            | 404                                                      |
| 13 | SpinDec                                                                                                                                 |       |       |       |         |             | http://bitbucket.org/sbalian/spindec                                                      | 404                                                      |
| 14 | sqct - Single qubit circuit toolkit                                                                                                     |       |       |       |         |             | http://code.google.com/p/sqct/ http://arxiv.org/abs/1206.5236                             | nebraska                                                 |
| 15 | MQT-DDSIM (formerly known as JKQ-DDSIM)                                                                                                 | x     |       |       |         | c++/python  | https://www.cda.cit.tum.de/research/quantum_simulation/                                   | s/qiskit-aer/ddsim,qasm                                  |
| 16 | QWIRE                                                                                                                                   |       |       |       |         |             | https://github.com/inQWIRE/QWIRE                                                          | nebraska                                                 |
| 17 | LIQUiD                                                                                                                                  |       |       |       |         | F#          | https://github.com/StationQ/Liquid                                                        | nebraska                                                 |
| 18 | Quantum Programming Studio                                                                                                              | x     | >     | >     |         | js/python   | https://quantum-circuit.com                                                               | web,weak,transpiler:openqasm,pyquil,quil,qiskit,cirq     |
| 19 | Qubit Workbench                                                                                                                         |       |       |       |         |             | https://elyah.io/product                                                                  | proprietary                                              |
| 20 | Linear Al                                                                                                                               |       |       |       |         |             | http://linearal.sourceforge.net/                                                          | nebraska                                                 |
| 21 | QCAD                                                                                                                                    |       |       |       |         |             | http://qcad.sourceforge.jp/                                                               | windows,404                                              |
| 22 | Quantum Computer Emulator                                                                                                               |       |       |       |         |             | http://www.compphys.org/QCE/                                                              | nebraska                                                 |
| 23 | Quantum Fog                                                                                                                             |       |       |       |         |             | https://github.com/artiste-qb-net/quantum-fog                                             | nebraska                                                 |
| 24 | SimQubit                                                                                                                                |       |       |       |         |             | http://sourceforge.net/projects/simqubit/                                                 | nebraska                                                 |
| 25 | Q-Kit                                                                                                                                   |       |       |       |         |             | https://sites.google.com/view/quantum-kit/home                                            | nebraska                                                 |
| 26 | jSQ- Java Quantique Simulator                                                                                                           |       |       |       |         |             | http://sourceforge.net/projects/simu-quantique/                                           | nebraska                                                 |
| 27 | Quantomatic                                                                                                                             |       |       |       |         |             | http://quantomatic.github.io/                                                             | nebraska                                                 |
| 28 | qMIPS101                                                                                                                                |       |       |       |         |             | http://institucional.us.es/qmipsmaster/                                                   | nebraska                                                 |
| 29 | Squankum                                                                                                                                |       |       |       |         |             | http://www.pha.jhu.edu/~jeffwass/squankum/ https://github.com/jeffwass/Squankum           | nebraska                                                 |
| 30 | Strange                                                                                                                                 |       |       |       |         |             | https://github.com/qcjava/strange                                                         | nebraska                                                 |
| 31 | BackupBrain Quantum Computer Simulator - Open-Source Programmable Quantum Computer Simulator implemented in client-side only JavaScript |       |       |       |         |             | https://backupbrain.github.io/quantum-compiler-simulator/                                 | nebraska                                                 |
| 32 | quantum-circuit - Quantum circuit simulator implemented in javascript                                                                   | x     | >     | >     |         | js/python   | https://www.npmjs.com/package/quantum-circuit                                             | web,weak,transpiler:openqasm,pyquil,quil,qiskit,cirq     |
| 33 | jsqis - Javascript Quantum Information Simulator                                                                                        |       |       |       |         |             | https://github.com/garrison/jsqis                                                         | nebraska                                                 |
| 34 | QSWalk.jl                                                                                                                               |       |       |       |         |             | https://github.com/QuantumWalks/QSWalk.jl                                                 | nebraska                                                 |
| 35 | QuantumOptics.jl                                                                                                                        |       |       |       |         |             | https://qojulia.org/                                                                      | unfit                                                    |
| 36 | QuantumWalk                                                                                                                             |       |       |       |         |             | https://github.com/QuantumWalks/QuantumWalk.jl                                            | nebraska                                                 |
| 37 | FEYNMAN                                                                                                                                 |       |       |       |         |             | http://cpc.cs.qub.ac.uk/summaries/ADWE                                                    | 404,nebraska                                             |
| 38 | Quantavo                                                                                                                                |       |       |       |         |             | http://www3.imperial.ac.uk/quantuminformation/research/downloads                          | 404                                                      |
| 39 | QDENSITY                                                                                                                                |       |       |       |         |             | http://www.pitt.edu/~tabakin/QDENSITY/                                                    | nebraska                                                 |
| 40 | Quantum                                                                                                                                 |       |       |       |         |             | http://homepage.cem.itesm.mx/lgomez/quantum/index.htm                                     | proprietary                                              |
| 41 | QuantumUtils                                                                                                                            |       |       |       |         |             | https://github.com/QuantumUtils/quantum-utils-mathematica                                 | proprietary                                              |
| 42 | Quantum Information Programs in Mathematica                                                                                             |       |       |       |         |             | http://quantum.phys.cmu.edu/QPM/                                                          | proprietary                                              |
| 43 | QuCalc                                                                                                                                  |       |       |       |         |             | http://crypto.cs.mcgill.ca/QuCalc/                                                        | proprietary                                              |
| 44 | QI                                                                                                                                      |       |       |       |         |             | https://github.com/iitis/qi                                                               | proprietary                                              |
| 45 | TRQS                                                                                                                                    |       |       |       |         |             | http://www.iitis.pl/~miszczak/trqs                                                        | proprietary                                              |
| 46 | drqubit                                                                                                                                 |       |       |       |         |             | http://www.dr-qubit.org/matlab.php                                                        | proprietary                                              |
| 47 | QC simulator                                                                                                                            |       |       |       |         |             | http://www-m3.ma.tum.de/twiki/bin/view/Software/QCWebHome                                 | proprietary                                              |
| 48 | QCTOOLS                                                                                                                                 |       |       |       |         |             | http://physics.berkeley.edu/research/haeffner/teaching/exp-quant-info/exp-quant-info      | 404                                                      |
| 49 | QETLAB                                                                                                                                  |       |       |       |         |             | http://www.qetlab.com                                                                     | proprietary                                              |
| 50 | QLib                                                                                                                                    |       |       |       |         |             | http://www.tau.ac.il/~quantum/qlib/qlib.html                                              | proprietary                                              |
| 51 | Quantum Computing Functions for Matlab (QFC)                                                                                            |       |       |       |         |             | http://www.robots.ox.ac.uk/~charles/                                                      | proprietary                                              |
| 52 | Qubit4matlab                                                                                                                            |       |       |       |         |             | http://bird.szfki.kfki.hu/~toth/qubit4matlab.html                                         | proprietary                                              |
| 53 | Quantum.NET                                                                                                                             |       |       |       |         |             | https://github.com/phbaudin/quantum-computing                                             | nebraska                                                 |
| 54 | GQC                                                                                                                                     |       |       |       |         |             | http://www.physics.uq.edu.au/gqc/                                                         | 404                                                      |
| 55 | QRBGS                                                                                                                                   |       |       |       |         |             | http://random.irb.hr/                                                                     | unfit,true-randomness                                    |
| 56 | Cirq                                                                                                                                    | x!    | x!    | x     | x       | python      | https://github.com/quantumlib/Cirq                                                        | google,cuda                                              |
| 57 | ProjectQ                                                                                                                                | x     |       | x     |         | python      | https://projectq.ch/                                                                      | eth-zurich,ibm                                           |
| 58 | QCircuits                                                                                                                               |       |       |       |         |             | http://www.awebb.info/qcircuits/index.html                                                | nebraska                                                 |
| 59 | QISKit                                                                                                                                  | x!    | x!    | x     | x       | python/c++  | https://qiskit.org/                                                                       | ibm,,qiskit-aer,openmp,cuda                              |
| 60 | qitensor                                                                                                                                |       |       |       |         |             | http://www.stahlke.org/dan/qitensor                                                       | nebraska                                                 |
| 61 | QuaEC                                                                                                                                   |       |       |       |         |             | http://www.cgranade.com/python-quaec/                                                     | unfit,error-correction                                   |
| 62 | QuTiP                                                                                                                                   | x     |       |       |         | python      | http://qutip.org/                                                                         | indipendent,open-system,openmp                           |
| 63 | sparse_pauli                                                                                                                            |       |       |       |         |             | https://github.com/bcriger/sparse_pauli                                                   | nebraska                                                 |
| 64 | toqito                                                                                                                                  |       |       |       |         |             | https://vprusso.github.io/toqito/                                                         | nebraska                                                 |
| 65 | SymQC                                                                                                                                   |       |       |       |         |             | https://gitee.com/quingo/SymQC                                                            | unfit,chinese-devs,gitee                                 |
| 66 | OpenQASM                                                                                                                                | <     | <     | <     | <       | python      | https://github.com/Qiskit/openqasm                                                        | ibm,qiskit                                               |
| 67 | QCGPU                                                                                                                                   | x     | x     |       |         | rust/python | https://qcgpu.github.io/                                                                  | openqasm,opencl,nebraska                                 |
| 68 | QIO                                                                                                                                     |       |       |       |         |             | http://hackage.haskell.org/package/QIO                                                    | nebraska                                                 |
| 69 | QML                                                                                                                                     |       |       |       |         |             | http://sneezy.cs.nott.ac.uk/qml/                                                          | 404                                                      |
| 70 | Quipper                                                                                                                                 |       |       |       |         |             | http://www.mathstat.dal.ca/~selinger/quipper/                                             | nebraska,unfit                                           |
| 71 | qchas                                                                                                                                   |       |       |       |         |             | https://hackage.haskell.org/package/qchas                                                 | nebraska                                                 |
#### Active simulators with desired feats
|    | name                                                                  | cpu   | gpu   | qpu   | qudit   | lang       | webpage                                                                                   | tags                                                     |
|---:|:----------------------------------------------------------------------|:------|:------|:------|:--------|:-----------|:------------------------------------------------------------------------------------------|:---------------------------------------------------------|
|  0 | Intel Quantum Simulator (IQS, former qHiPSTER)                        | x!    |       |       |         | c++/python | https://github.com/iqusoft/intel-qs https://arxiv.org/abs/2001.10554                      | intel,mpi,mkl                                            |
|  1 | staq                                                                  | >     | >     | >     |         | c++/python | https://github.com/softwareqinc/staq                                                      | openqasm,device_mapper,transpiler:quil,projectq,q#,circq |
|  2 | QuEST                                                                 | x!    | x!    | >     |         | c++/c      | https://quest.qtechtheory.org https://arxiv.org/abs/1802.08032                            | cuda,openmp,mpi,qasm                                     |
|  3 | Scaffold/ScaffCC                                                      | >     |       | >     |         | c++/c      | https://www.cs.princeton.edu/research/techreps/TR-934-12 https://github.com/epiqc/ScaffCC | scaffold_dsl,compiler,qasm                               |
|  4 | Qrack                                                                 | x     | x     |       |         | c++/python | https://vm6502q.readthedocs.io                                                            | opencl,s/qiskit-aer/qrack,s/projectq/qrack               |
|  5 | Quantum++                                                             | x     |       |       |         | c++/python | https://github.com/softwareQinc/qpp                                                       | openmp,eign3                                             |
|  6 | MQT-DDSIM (formerly known as JKQ-DDSIM)                               | x     |       |       |         | c++/python | https://www.cda.cit.tum.de/research/quantum_simulation/                                   | s/qiskit-aer/ddsim,qasm                                  |
|  7 | Quantum Programming Studio                                            | x     | >     | >     |         | js/python  | https://quantum-circuit.com                                                               | web,weak,transpiler:openqasm,pyquil,quil,qiskit,cirq     |
|  8 | quantum-circuit - Quantum circuit simulator implemented in javascript | x     | >     | >     |         | js/python  | https://www.npmjs.com/package/quantum-circuit                                             | web,weak,transpiler:openqasm,pyquil,quil,qiskit,cirq     |
|  9 | Cirq                                                                  | x!    | x!    | x     | x       | python     | https://github.com/quantumlib/Cirq                                                        | google,cuda                                              |
| 10 | ProjectQ                                                              | x     |       | x     |         | python     | https://projectq.ch/                                                                      | eth-zurich,ibm                                           |
| 11 | QISKit                                                                | x!    | x!    | x     | x       | python/c++ | https://qiskit.org/                                                                       | ibm,,qiskit-aer,openmp,cuda                              |
| 12 | QuTiP                                                                 | x     |       |       |         | python     | http://qutip.org/                                                                         | indipendent,open-system,openmp                           |
| 13 | OpenQASM                                                              | <     | <     | <     | <       | python     | https://github.com/Qiskit/openqasm                                                        | ibm,qiskit                                               |
### From internet search
#### Simulators with desired feats
|    | name          | cpu   | gpu   | qpu   | qudit   | status   | lang             | webpage                                         | tags                                            |
|---:|:--------------|:------|:------|:------|:--------|:---------|:-----------------|:------------------------------------------------|:------------------------------------------------|
|  0 | pyquil        | x     |       | x     |         | active   | python           | https://github.com/rigetti/pyquil               | righetti,quil,forest,quil-T,qutrit              |
|  1 | aws-braket    | x!    | x!    | x     |         | active   | c++/python       | https://github.com/aws/amazon-braket-sdk-python | amazon,aws-cloud,pennylane-plugin,lightning.gpu |
|  2 | azure-quantum | x     |       | x     |         | active   | c#/dotnet/python | https://learn.microsoft.com/en-us/azure/quantum | microsoft,azure-cloud,windows                   |