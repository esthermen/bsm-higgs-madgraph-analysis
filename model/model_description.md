Two-Higgs-Doublet Model Extension – Computational Study
1. Theoretical Framework

This project implements a Beyond the Standard Model (BSM) extension featuring a Two-Higgs-Doublet Model (2HDM), motivated by the limitations of the Standard Model in explaining electroweak symmetry breaking and scalar sector structure.

The model introduces:

Two scalar doublets

Two physical neutral Higgs bosons:

A lighter scalar (identified with the 125 GeV Higgs)

A heavier scalar state

The scalar potential includes additional interaction terms that modify production cross-sections and decay channels compared to the Standard Model.

The work is based on the theoretical formulation developed in my undergraduate thesis, where the phenomenological consequences of the extended Higgs sector were analyzed using numerical simulation tools.

2. Computational Approach

The study was carried out using:

MadGraph for event generation

Numerical post-processing in Python

Cross-section extraction from generated event files

The workflow consists of:

Model implementation in MadGraph

Definition of production channels

Generation of parton-level events

Extraction of cross-sections

Numerical analysis and comparison with Standard Model predictions

3. Numerical Objectives

The main computational goals are:

Evaluate production cross-sections for scalar bosons

Compare heavy vs light Higgs behavior

Analyze deviations from Standard Model expectations

Study parameter dependence of the extended scalar sector

4. Research Context

This study represents an original computational analysis: the specific parameter configuration and cross-section comparison performed in this work had not been previously calculated within the research group.

The implementation required:

Understanding the theoretical scalar potential

Translating theoretical couplings into simulation inputs

Interpreting numerical outputs physically

5. Repository Scope

This repository contains:

Python scripts for post-processing MadGraph outputs

Data parsing tools

Cross-section comparison routines

Visualization of results

The objective is to present the work as a reproducible computational physics project, emphasizing numerical modeling, physical interpretation, and simulation methodology.
