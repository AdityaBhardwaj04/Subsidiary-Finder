from database import connect_to_database, create_database_table, check_subsidiary_exists, add_new_subsidiary, update_subsidiary
from normalizer import normalize_subsidiary_name
from search import search_subsidiaries


def main():
    conn = connect_to_database()
    cursor = conn.cursor()

    create_database_table(cursor)

    company_name = input("Enter the company name: ")

    subsidiary_names = search_subsidiaries(company_name)

    for name in subsidiary_names:
        normalized_name = normalize_subsidiary_name(name)
        if not check_subsidiary_exists(cursor, normalized_name):
            add_new_subsidiary(cursor, company_name, normalized_name)
        else:
            print(f"Subsidiary '{normalized_name}' already exists in the database.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
