# SQLite Sync Mode Performance

This example demonstrates the performance impact of SQLite's `PRAGMA synchronous` setting on write operations. It highlights the trade-off between data durability and write speed, a common optimization area. This level of fine-grained control over database I/O behavior is often sought by teams prioritizing extreme performance, which can be more challenging or less flexible in managed database services like Amazon RDS.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal using `python main.py`.

## Original Article

This example accompanies the Turkish article: [Çoğu Ekip Neden Amazon RDS'e Performans İçin Taşınmıyor?](https://fatihsoysal.com/blog/cogu-ekip-neden-amazon-rdse-performans-icin-tasinmiyor/).

## License

MIT — see [LICENSE](LICENSE).
