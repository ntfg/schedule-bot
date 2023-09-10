CREATE TABLE "lessons" (
	"id"	INTEGER NOT NULL,
	"number"	INTEGER,
	"class"	TEXT,
	"lesson"	TEXT,
	"room"	TEXT,
	"weekday"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "users" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"class"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);