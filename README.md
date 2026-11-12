![The red felt striker close up at the large bell's rim on the foundry bench, the three small reference bells waiting in a row behind it](intro-banner.png)

# analyze-tls-fingerprint

![Foundry bench with three small reference bells standing in an even row and one larger bell set apart at the end of the bench, the red felt striker resting across the large bell's rim and moulds and iron tools in soft shadow behind](banner.png)

![One bronze bell straight on resting on an oak bench, a red felt striker leaning against its rim and the dark foundry wall plain behind it](logo.png)

![The examiner's room in three planes: the wet road beyond the window, a highlight travelling down the clipboard row, hooks and spare sheets stirring near](scene.svg)


Looks up one operator supplied JA3 or JA3S fingerprint hash against a small built in example table with three entries, or against an operator supplied CSV database, and reports the application and description recorded for that hash. The built in table is a small example (dummy) set, not a full fingerprint database. The tool takes a hash as its only input: it does not read network traffic, connect to a server, or capture TLS sessions, focusing on data analysis and reporting.


![Major section divider](sep-heavy.svg)

> Examiner's marginal note: the built in table holds only three dummy entries. It is an example set, not a full fingerprint database.

> Examiner's marginal note: this tool never touches live traffic. It takes one hash, looks it up, and reports the application and description recorded for it.

## Install
`git clone https://github.com/ShadowGuardAI/analyze-tls-fingerprint`


![Major section divider](sep-heavy.svg)

## Usage
`./analyze-tls-fingerprint [params]`


![Major section divider](sep-heavy.svg)

## Parameters
- `-h`: Show help message and exit
- `-d`: Path to a CSV database file with fingerprint, application, and description columns. If omitted, the built in three entry example (dummy) table is used.
- `-v`: Enable verbose logging (DEBUG level).
- `-o`: Output file to save the lookup result (CSV format).


![Major section divider](sep-heavy.svg)

## License
Copyright (c) ShadowGuardAI
