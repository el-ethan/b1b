-- SQL for the ChFont table

BEGIN TRANSACTION;
DROP TABLE IF EXISTS ChFont;

CREATE TABLE ChFont(id INTEGER PRIMARY KEY,
                    font VARCHAR(50),
                    type VARCHAR(2),
                    platform VARCHAR(20));
INSERT INTO ChFont VALUES(1, 'Yuppy TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(2, 'Yuppy SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(3, 'Yuanti SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(4, 'Xingkai SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(5, 'Weibei TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(6, 'Weibei SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(7, 'Wawati TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(8, 'Wawati SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(9, 'Songti TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(10, 'Songti SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(11, 'MingLiU_HKSCS-ExtB', 'SC', 'OSX');
INSERT INTO ChFont VALUES(12, 'MingLiU_HKSCS', 'SC', 'OSX');
INSERT INTO ChFont VALUES(13, 'Libian SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(14, 'Lantinghei TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(15, 'Lantinghei SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(16, 'Kaiti TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(17, 'Kaiti SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(18, 'Heiti TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(19, 'Heiti SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(20, 'HanziPen TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(21, 'HanziPen SC', 'SC', 'OSX');
INSERT INTO ChFont VALUES(22, 'Hannotate TC', 'TC', 'OSX');
INSERT INTO ChFont VALUES(23, 'Hannotate SC', 'SC', 'OSX');
COMMIT;