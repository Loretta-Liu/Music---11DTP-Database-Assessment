# Loretta Liu - Music Charts Database Application

import sqlite3
import os

#Constants and Variables
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'music.db')

# Database file
DATABASE = "music.db"


def check_table_exists():
    """Check if the music table exists"""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table' AND name='music';
    """)

    table = cursor.fetchone()

    conn.close()

    return table is not None


def display_all_music():
    """Display all music records"""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM music")
    results = cursor.fetchall()

    print("\nALL MUSIC RECORDS")
    print("-" * 70)

    for music in results:
        print(music)

    conn.close()


def display_top_rankings():
    """Display top 5 ranked songs"""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT artist_name, song_name, chart_ranking
    FROM music
    ORDER BY chart_ranking ASC
    LIMIT 5
    """)

    results = cursor.fetchall()

    print("\nTOP 5 CHART RANKINGS")
    print("-" * 30)

    for row in results:
        print(row)

    conn.close()


def display_most_streamed():
    """Display top 3 streamed songs"""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT artist_name, song_name, song_streams
    FROM music
    ORDER BY song_streams DESC
    LIMIT 3
    """)

    results = cursor.fetchall()

    print("\nMOST STREAMED SONGS")
    print("-" * 30)

    for row in results:
        print(row)

    conn.close()


def search_artist():
    """Search for an artist"""

    artist = input("Enter artist name: ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM music
    WHERE artist_name = ?
    """, (artist,))

    results = cursor.fetchall()

    if len(results) == 0:
        print("Artist not found.")
    else:
        for row in results:
            print(row)

    conn.close()


# Main Program

if not check_table_exists():
    print("ERROR: The table 'music' does not exist in music.db")
    print("Open SQLiteStudio and check the table name.")
else:

    while True:

        print("\nMusic Charts Database")
        print("1. Display all music")
        print("2. Display top rankings")
        print("3. Display most streamed songs")
        print("4. Search artist")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_all_music()

        elif choice == "2":
            display_top_rankings()

        elif choice == "3":
            display_most_streamed()

        elif choice == "4":
            search_artist()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
