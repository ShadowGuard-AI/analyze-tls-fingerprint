import argparse
import logging
import pandas as pd
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dummy JA3/JA3S database (replace with a real one)
JA3_DATABASE = {
    "839cca7d4f505a770746e8a593448bb6": {"application": "curl", "description": "Standard curl client"},
    "771c2b011b35a8373f5202ca27659bb0": {"application": "OpenSSL", "description": "Generic OpenSSL client"},
    "d4e185393f7d6875a4795151712043bb": {"application": "Chrome", "description": "Chrome browser (desktop)"},
}


def setup_argparse():
    """
    Sets up the argument parser for the command-line interface.

    Returns:
        argparse.ArgumentParser: The argument parser object.
    """
    parser = argparse.ArgumentParser(description="Looks up a JA3 or JA3S fingerprint hash in a built in three entry example table or an operator supplied CSV database.")
    parser.add_argument("fingerprint", help="The JA3 or JA3S fingerprint hash to look up.")
    parser.add_argument("-d", "--database", help="Path to the JA3/JA3S database file (CSV).  Defaults to the built in three entry example (dummy) table.", required=False) # Optional database path
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging (DEBUG level).")
    parser.add_argument("-o", "--output", help="Output file to save the analysis results (CSV format).", required=False)

    return parser


def load_database(db_path=None):
    """
    Loads the JA3/JA3S database from a CSV file.

    Args:
        db_path (str, optional): The path to the CSV database file. Defaults to None,
            in which case a hardcoded dummy database is used.

    Returns:
        dict: A dictionary representing the JA3/JA3S database, where keys are fingerprints
            and values are dictionaries containing application and description information.
    """
    if db_path:
        try:
            df = pd.read_csv(db_path)
            # Assuming the CSV has columns 'fingerprint', 'application', and 'description'
            # Keys are normalised the same way lookups are (see
            # analyze_fingerprint), so a CSV written with upper case or
            # padded hashes still matches.
            # A fingerprint listed twice in the CSV keeps only its
            # last row, silently. There is no warning because a dict
            # comprehension has nowhere to put one; anyone curating a
            # database file should know the earlier row is gone.
            db = {str(row['fingerprint']).strip().lower(): {'application': row['application'], 'description': row['description']}
                for index, row in df.iterrows()}
            logging.info(f"Loaded JA3/JA3S database from {db_path}")
            return db
        except FileNotFoundError:
            logging.error(f"Database file not found: {db_path}")
            print(f"Error: Database file not found: {db_path}")
            sys.exit(1)
        except pd.errors.EmptyDataError:
            logging.error(f"Database file is empty: {db_path}")
            print(f"Error: Database file is empty: {db_path}")
            sys.exit(1)
        except KeyError as e:
            logging.error(f"Database file missing required column: {e}")
            print(f"Error: Database file missing required column: {e}")
            sys.exit(1)
        except Exception as e:
            logging.error(f"Error loading database file: {e}")
            print(f"Error loading database file: {e}")
            sys.exit(1)


    else:
        logging.info("Using internal dummy JA3/JA3S database.")
        return JA3_DATABASE


def analyze_fingerprint(fingerprint, database):
    """
    Analyzes a given JA3/JA3S fingerprint against the provided database.

    Args:
        fingerprint (str): The JA3 or JA3S fingerprint to analyze.
        database (dict): The JA3/JA3S database (dictionary).

    Returns:
        dict: A dictionary containing the analysis results.  Returns None if not found.
    """
    # A JA3 hash is an MD5 hex digest. Hex digests compare case
    # insensitively and databases publish them in lower case, while tools
    # often print them in upper case, so the lookup key is normalised once
    # here. A malformed fingerprint raises instead of returning None,
    # because None also means "valid but unknown" and the two cases need
    # different exit codes in main.
    fingerprint = fingerprint.strip().lower()
    if len(fingerprint) != 32:
        raise ValueError("Invalid fingerprint length.  Must be 32 characters (MD5 hash).")
    int(fingerprint, 16)  # Raises ValueError if it is not a hexadecimal string.

    # JA3 and JA3S share this one table and one lookup. Nothing asks
    # whether the hash came from a client hello or a server hello, so
    # an entry recorded for one kind answers for the other whenever
    # the strings happen to collide in the same file.
    # Perform the analysis
    if fingerprint in database:
        analysis_result = database[fingerprint]
        logging.info(f"Fingerprint {fingerprint} found in database. Application: {analysis_result['application']}")
        return analysis_result
    else:
        logging.info(f"Fingerprint {fingerprint} not found in database.")
        return None



def save_results_to_csv(results, output_file):
    """
    Saves the analysis results to a CSV file.

    Args:
        results (dict): The analysis results to save.
        output_file (str): The path to the output CSV file.
    """
    try:
        df = pd.DataFrame([results])  # Convert dictionary to DataFrame
        df.to_csv(output_file, index=False)
        logging.info(f"Analysis results saved to {output_file}")
        return True
    except Exception as e:
        logging.error(f"Error saving results to CSV: {e}")
        print(f"Error: Error saving results to CSV: {e}")
        return False

def main():
    """
    The main function of the script.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Verbose logging enabled.")

    database = load_database(args.database)

    # Analyze the fingerprint
    try:
        analysis_result = analyze_fingerprint(args.fingerprint, database)
    except ValueError as e:
        logging.error(f"Invalid fingerprint format: {e}")
        print(f"Error: Invalid fingerprint format: {e}")
        sys.exit(1)

    if analysis_result:
        print(f"Fingerprint: {args.fingerprint}")
        print(f"  Application: {analysis_result['application']}")
        print(f"  Description: {analysis_result['description']}")

        if args.output:
            # Prepare data for CSV output.  Ensure all fields are present.
            output_data = {
                'fingerprint': args.fingerprint,
                'application': analysis_result['application'],
                'description': analysis_result['description']
            }
            if not save_results_to_csv(output_data, args.output):
                sys.exit(1)
    else:
        # Not found is a normal answer here, not a failure, so the
        # exit code is 0. With the built in three entry table that is
        # the answer nearly every real fingerprint gets, which is why
        # the help text calls the table an example.
        print(f"Fingerprint {args.fingerprint} not found in database.")


if __name__ == "__main__":
    main()