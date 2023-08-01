CREATE TABLE "Users" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);


CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (`action`, `admin_id`, `approver_one_id`)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO "Categories" VALUES (null, 'News');
INSERT INTO "Categories" VALUES (null, 'Videos');
INSERT INTO "Categories" VALUES (null, 'Photos');
INSERT INTO "Categories" VALUES (null, 'Guides');
INSERT INTO "Categories" VALUES (null, 'Books');


INSERT INTO "Tags" VALUES (null, 'JavaScript');
INSERT INTO "Tags" VALUES (null, 'React');
INSERT INTO "Tags" VALUES (null, 'Bootstrap');
INSERT INTO "Tags" VALUES (null, 'Python');
INSERT INTO "Tags" VALUES (null, 'Cats');
INSERT INTO "Tags" VALUES (null, 'Bubbles');
INSERT INTO "Tags" VALUES (null, 'Tailwind');
INSERT INTO "Tags" VALUES (null, 'SciFi');


INSERT INTO "Users" VALUES (null, "Chesney", "Hardin", "chesneyhardin@aol.com", "I like turtles", "ChesneyHardin101", "password856", "https://gratisography.com/wp-content/uploads/2022/05/gratisography-heavenly-free-stock-photo.jpg", "2020-04-04", 1);
INSERT INTO "Users" VALUES (null, "Daniel", "Myers", "DanielMyers@aol.com", "I really like turtles", "DanielMyers101", "paord", "https://jenmulligandesign.com/wp-content/uploads/2017/04/pexels-beach-tropical-scene-free-stock-photo.jpg", "2023-04-02", 1);
INSERT INTO "Users" VALUES (null, "Ryan", "Phillips", "ryanPhilips@aol.com", "I like alligators", "RyanHPhillips231", "prd", "https://img.freepik.com/free-photo/digital-painting-mountain-with-colorful-tree-foreground_1340-25699.jpg", "2021-11-11", 1);
INSERT INTO "Users" VALUES (null, "Cassie", "Revell", "CassieRevell@aol.com", "I really like cats", "CassieRevell101", "word", "https://static.vecteezy.com/system/resources/thumbnails/008/749/779/small/cat-blue-eyes-in-summer-animal-concept-free-photo.jpg", "2030-04-09", 1);
INSERT INTO "Users" VALUES (null, "Jonathan", "VanDuyne", "IamLame@aol.com", "I am lame", "lameguy", "passwd", "https://cdn.pixabay.com/photo/2023/06/04/11/42/river-8039447_1280.jpg", "2024-04-09", 1);
INSERT INTO "Users" VALUES (null, "Belle", "Hollander", "Kenergy@aol.com", "I thought of the name Kenergy", "Kenergy10101", "pa75d", "https://img.freepik.com/free-photo/happy-bunny-with-many-easter-eggs-grass-festive-background-decorative-design_90220-1091.jpg", "2021-02-11", 1);
INSERT INTO "Users" VALUES (null, "Lance", "Buckley", "LameLance@aol.com", "I am Lance, and I'm not wearing pants", "LanceNoChancesad", "p12ord", "https://static.vecteezy.com/system/resources/thumbnails/006/180/166/small/panther-chameleon-on-branch-free-photo.jpg", "2024-12-11", 1);
INSERT INTO "Users" VALUES (null, "Sam", "Thrasher", "SamThrasher@aol.com", "I am guilty by associaton like Adam Banks in Mighty Ducks 3", "SamThrashing13234", "p985245632", "https://cdn.pixabay.com/photo/2023/06/16/21/13/landscape-8068793_640.jpg", "2014-01-01", 1);


INSERT INTO "Reactions" VALUES (null, 'happy', 'https://pngtree.com/so/happy');
INSERT INTO "Reactions" VALUES (null, 'laugh', 'https://pngtree.com/freepng/open-mouth-laughing-expression-illustration_4676475.html');
INSERT INTO "Reactions" VALUES (null, 'embarrassed', 'https://png.pngtree.com/element_our/png/20181227/emoticons-stickers-rabbit-be-embarrassed-png_301809.jpg');
INSERT INTO "Reactions" VALUES (null, 'you suck', 'https://pngtree.com/freepng/vector-cartoon-stick-figure-drawing-conceptual-illustration-of-mad-or-crazy-man-or-person-holding-you-suck-sign_8427005.html');
INSERT INTO "Reactions" VALUES (null, 'Alien Party', 'https://png.pngtree.com/png-vector/20220610/ourmid/pngtree-pink-and-yellow-one-eyed-party-monster-with-a-party-hat-png-image_4828405.png');
INSERT INTO "Reactions" VALUES (null, 'sad', 'https://pngtree.com/freepng/hand-drawn-illustration-cartoon-creative-emoticon-pack-design-crying_5497862.html');
INSERT INTO "Reactions" VALUES (null, 'stop!', 'https://pngtree.com/freepng/red-palm-and-stop-sign-in-red-hexagon_5489514.html');


INSERT INTO "Subscriptions" VALUES (null, 1, 2, "2014-01-01");
INSERT INTO "Subscriptions" VALUES (null, 2, 6, "2012-09-09");
INSERT INTO "Subscriptions" VALUES (null, 3, 7, "2023-03-09");
INSERT INTO "Subscriptions" VALUES (null, 4, 5, "2013-03-07");
INSERT INTO "Subscriptions" VALUES (null, 5, 3, "2021-01-04");
INSERT INTO "Subscriptions" VALUES (null, 6, 8, "2021-01-04");
INSERT INTO "Subscriptions" VALUES (null, 5, 2, "2001-01-04");
INSERT INTO "Subscriptions" VALUES (null, 2, 3, "2005-02-04");
INSERT INTO "Subscriptions" VALUES (null, 6, 1, "1901-06-04");


INSERT INTO "Posts" VALUES (null, 1, 2, "How to turn your living room into a ball pit", "2022-12-29", "",
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, 
eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem 
quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.", 1);
INSERT INTO "Posts" VALUES (null, 2, 3, "The trick to finding the best Aldi Finds that Aldi doesn't want you to find out about!", "2023-01-12", "", "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.", 1);
INSERT INTO "Posts" VALUES (null, 3, 1, "Zig Zag", "2023-01-29", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbestanimations.com%2FMusic%2FDancers%2Ffunny-dance%2Ffunny-dance-dancing-animated-gif-image-11.gif&f=1&nofb=1&ipt=85fcee1d7fc28b30309e1e6746cdc2612b52f51e38d7dc25e823f7f118cd7de4&ipo=images", "My smooth moves.", 1);
INSERT INTO "Posts" VALUES (null, 5, 4, "JonathanDumboFod", "1903-66-06", "https://www.refinery29.com/images/11419423.jpg?format=webp&width=720&height=864&quality=85", "I looked like Zuko during my headshot.", 1);
INSERT INTO "Posts" VALUES (null, 6, 1, "webegg", "1943-66-06", "https://www.refinery29.com/images/11419423.jpg?format=webp&width=720&height=864&quality=85", "I eggman yo.", 1);
INSERT INTO "Posts" VALUES (null, 6, 3, "wteeee", "1013-66-06", "https://www.refinery29.com/images/11419423.jpg?format=webp&width=720&height=864&quality=85", "I yo.", 1);
INSERT INTO "Posts" VALUES (null, 7, 5, "peggg", "2003-06-06", "https://www.refinery29.com/images/11419423.jpg?format=webp&width=720&height=864&quality=85", "I peg yo.", 1);
INSERT INTO "Posts" VALUES (null, 1, 3, "How to turn into a ball pit", "2020-12-29", "",
"Sed ut perspi.", 1);


INSERT INTO "PostReactions" VALUES (null, 1, 3, 1);
INSERT INTO "PostReactions" VALUES (null, 2, 5, 2);
INSERT INTO "PostReactions" VALUES (null, 3, 6, 3);
INSERT INTO "PostReactions" VALUES (null, 4, 8, 3);
INSERT INTO "PostReactions" VALUES (null, 5, 7, 3);
INSERT INTO "PostReactions" VALUES (null, 6, 4, 2);
INSERT INTO "PostReactions" VALUES (null, 1, 2, 1);
INSERT INTO "PostReactions" VALUES (null, 7, 1, 2);


INSERT INTO "Comments" VALUES (null, 1, 1, "amazzzzzzzzzzzzzzing!");
INSERT INTO "Comments" VALUES (null, 2, 2, "this sucks ass!");
INSERT INTO "Comments" VALUES (null, 3, 3, "severely lacking Kenergy");
INSERT INTO "Comments" VALUES (null, 1, 4, "so good I wanted to cry");
INSERT INTO "Comments" VALUES (null, 2, 7, "can't");

DELETE FROM Subscriptions WHERE id = 14;


SELECT DISTINCT
    p.id,
    u.username AS author_username,
    p.image_url,
    p.publication_date,
    p.title,
    ct.label AS category_label
FROM Subscriptions s
JOIN Users u ON s.author_id = u.id
JOIN Posts p ON u.id = p.user_id
JOIN Categories ct ON p.category_id = ct.id
WHERE s.follower_id = 2

SELECT DISTINCT
     s.follower_id, 
     s.author_id,
     p.category_id, 
     p.title,
     p.publication_date,
     p.image_url,
     p.content,
     p.approved
FROM Subscriptions s
JOIN Posts p ON p.user_id = s.author_id
WHERE s.follower_id = 2;

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved
FROM Posts p
JOIN Subscriptions s ON p.user_id = s.author_id
WHERE s.follower_id = 2

SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.bio,
    u.username,
    u.password,
    u.profile_image_url,
    u.created_on,
    u.active,
    s.follower_id
FROM Users u
LEFT JOIN Subscriptions s ON u.id = s.author_id
WHERE u.id = 5;

SELECT
    p.id,
    s.follower_id,
    u.username,
    p.image_url,
    p.publication_date,
    p.title,
    ct.label
FROM Subscriptions s
JOIN Posts p ON p.user_id = s.author_id
JOIN Users u ON p.user_id = u.id
JOIN Categories ct ON p.category_id = ct.id
WHERE s.follower_id = 5


SELECT
    c.id,
    c.post_id,
    c.author_id,
    c.content
FROM Comments c;

SELECT
    s.id,
    s.follower_id,
    s.author_id,
    s.created_on
FROM Subscriptions s;

SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.bio,
    u.username,
    u.password,
    u.profile_image_url,
    u.created_on,
    u.active
FROM Users u;

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved
FROM Posts p
WHERE p.user_id = 2;

SELECT
    r.id,
    r.label,
    r.image_url
FROM Reactions r;

SELECT
    pr.id,
    pr.user_id,
    pr.reaction_id,
    pr.post_id
FROM PostReactions pr;

SELECT
    t.id,
    t.label
FROM Tags t;

SELECT
    pt.id,
    pt.post_id,
    pt.tag_id
FROM PostTags pt;

SELECT
    ct.id,
    ct.label
FROM Categories ct;


 SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved,
    pt.tag_id, 
    t.label,
    t.id             
  FROM PostTags pt 
  Join Posts p, Tags t
  On pt.post_id = p.id AND pt.tag_id = t.id
  WHERE t.id = 2