author_book_totals = (
    session.query(
        Author.first_name,
        Author.last_name,
        func.count(Book.title).label("book_total")
    )
    .join(Book)
    .group_by(Author.last_name)
    .order_by(desc("book_total"))
    .all()
)
