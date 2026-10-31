![Banner](banner.png)

# analyze-tls-fingerprint
Looks up one operator supplied JA3 or JA3S fingerprint hash against a small built in example table with three entries, or against an operator supplied CSV database, and reports the application and description recorded for that hash. The built in table is a small example (dummy) set, not a full fingerprint database. The tool takes a hash as its only input: it does not read network traffic, connect to a server, or capture TLS sessions. - Focused on Data analysis and reporting

## Install
`git clone https://github.com/ShadowGuardAI/analyze-tls-fingerprint`

## Usage
`./analyze-tls-fingerprint [params]`

## Parameters
- `-h`: Show help message and exit
- `-d`: Path to a CSV database file with fingerprint, application, and description columns. If omitted, the built in three entry example (dummy) table is used.
- `-v`: Enable verbose logging (DEBUG level).
- `-o`: Output file to save the lookup result (CSV format).

## License
Copyright (c) ShadowGuardAI
