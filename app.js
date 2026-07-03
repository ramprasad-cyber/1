const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./gym.db');

db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS ram (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name VARCHAR(50),
      age INT
    )
  `);

  db.run('DELETE FROM ram');

  db.run(`
    INSERT INTO ram (id, name, age) VALUES
      (1, 'ram', 22),
      (2, 'nag', 29),
      (3, 'mahesh', 40)
  `);

  db.all('SELECT id, name, age FROM ram', (err, rows) => {
    if (err) {
      console.error(err.message);
      db.close();
      return;
    }

    console.log('Connected and loaded rows:');
    rows.forEach((row) => console.log(row));
    db.close();
  });
});
