
import sqlite3
import json

# Database connection setup
def get_database_connection():
    return sqlite3.connect('your_database.db')

# Process asset data
def process_asset(cursor, asset_data):
    ipv4 = asset_data['ipv4']
    hostname = asset_data['hostname']
    fqdn = asset_data['fqdn']

    # Check if the asset exists
    cursor.execute("SELECT id FROM assets WHERE ipv4 = ? AND hostname = ?", (ipv4, hostname))
    row = cursor.fetchone()

    if row:
        # Asset exists, update it
        asset_id = row[0]
        cursor.execute("UPDATE assets SET fqdn = ? WHERE id = ?", (fqdn, asset_id))
    else:
        # Asset does not exist, insert it
        cursor.execute("INSERT INTO assets (fqdn, ipv4, hostname) VALUES (?, ?, ?)", (fqdn, ipv4, hostname))
        asset_id = cursor.lastrowid

    return asset_id

# Process vulnerabilities data
def process_vulnerabilities(cursor, asset_id, vulnerability_data, state, seen_vulnerabilities):
    vendor_id = vulnerability_data['id']
    is_open = state

    # Check if the vulnerability exists
    cursor.execute("SELECT id FROM vulnerabilities WHERE asset_id = ? AND vendor_id = ?", (asset_id, vendor_id))
    row = cursor.fetchone()

    if row:
        # Vulnerability exists, update it
        cursor.execute("UPDATE vulnerabilities SET is_open = ? WHERE asset_id = ? AND vendor_id = ?", (is_open, asset_id, vendor_id))
    else:
        # Vulnerability does not exist, insert it
        cursor.execute("INSERT INTO vulnerabilities (asset_id, vendor_id, is_open) VALUES (?, ?, ?)", (asset_id, vendor_id, is_open))
    seen_vulnerabilities[asset_id].add(vulnerability_data['id'])

# Mark vulnerabilities as resolved
def mark_vulnerabilities_resolved(cursor, seen_vulnerabilities):
    for asset_id, current_vulnerabilities in seen_vulnerabilities.items():
        # Find all vulnerabilities for the asset
        cursor.execute("SELECT vendor_id FROM vulnerabilities WHERE asset_id = ?", (asset_id,))
        all_vulnerabilities = set(row[0] for row in cursor.fetchall())

        # Find vulnerabilities to be marked as resolved
        vulnerabilities_to_resolve = all_vulnerabilities - set(current_vulnerabilities)
        print("vulnerabilities_to_resolve: ", vulnerabilities_to_resolve)

        for vendor_id in vulnerabilities_to_resolve:
            cursor.execute("UPDATE vulnerabilities SET is_open = 'RESOLVED' WHERE asset_id = ? AND vendor_id = ?", (asset_id, vendor_id))

# Function to create the 'assets' table
def create_assets_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fqdn TEXT,
            ipv4 TEXT,
            hostname TEXT,
            UNIQUE(ipv4, hostname)
        )
    ''')

# Function to create the 'vulnerabilities' table
def create_vulnerabilities_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vulnerabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER,
            is_open TEXT,
            vendor_id TEXT,
            FOREIGN KEY (asset_id) REFERENCES assets (id),
            UNIQUE(asset_id, vendor_id)
        )
    ''')

# Main function to process incoming data
def process_incoming_data(json_array):
    conn = get_database_connection()
    cursor = conn.cursor()
    create_assets_table(cursor)
    create_vulnerabilities_table(cursor)
    conn.commit()
    from collections import defaultdict
    seen_vulnerabilities = defaultdict(set)  # Keeps track of seen vulnerabilities per asset

    try:
        for json_data in json_array:
            asset_data = json_data['asset']
            vulnerability_data = json_data['plugin']
            state = json_data["state"]
            asset_id = process_asset(cursor, asset_data)
            process_vulnerabilities(cursor, asset_id, vulnerability_data,state, seen_vulnerabilities)

        mark_vulnerabilities_resolved(cursor, seen_vulnerabilities)

        conn.commit()
    finally:
        conn.close()

# Load JSON array (replace with your actual JSON loading logic)
with open('scan_2.json', 'r') as f:
    json_array = json.load(f)
    # Process the incoming data
    process_incoming_data(json_array)
