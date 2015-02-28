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
INSERT INTO ChFont VALUES(24, 'Microsoft JhengHei', NULL, 'Win');
INSERT INTO ChFont VALUES(25, '@Microsoft JhengHei', NULL, 'Win');
INSERT INTO ChFont VALUES(26, 'Microsoft YaHei', NULL, 'Win');
INSERT INTO ChFont VALUES(27, '@Microsoft YaHei', NULL, 'Win');
INSERT INTO ChFont VALUES(28, 'MingLiU', NULL, 'Win');
INSERT INTO ChFont VALUES(29, '@MingLiU', NULL, 'Win');
INSERT INTO ChFont VALUES(30, 'PMingLiU', NULL, 'Win');
INSERT INTO ChFont VALUES(31, '@PMingLiU', NULL, 'Win');
INSERT INTO ChFont VALUES(32, 'MingLiU_HKSCS', NULL, 'Win');
INSERT INTO ChFont VALUES(33, '@MingLiU_HKSCS', NULL, 'Win');
INSERT INTO ChFont VALUES(34, 'MingLiU-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(35, '@MingLiU-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(36, 'PMingLiU-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(37, '@PMingLiU-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(38, 'MingLiU_HKSCS-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(39, '@MingLiU_HKSCS-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(40, 'Shruti', NULL, 'Win');
INSERT INTO ChFont VALUES(41, 'SimSun', NULL, 'Win');
INSERT INTO ChFont VALUES(42, '@SimSun', NULL, 'Win');
INSERT INTO ChFont VALUES(43, 'NSimSun', NULL, 'Win');
INSERT INTO ChFont VALUES(44, '@NSimSun', NULL, 'Win');
INSERT INTO ChFont VALUES(45, 'SimSun-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(46, '@SimSun-ExtB', NULL, 'Win');
INSERT INTO ChFont VALUES(47, 'Microsoft Tai Le', NULL, 'Win');
INSERT INTO ChFont VALUES(48, 'Microsoft Yi Baiti', NULL, 'Win');
INSERT INTO ChFont VALUES(49, 'FangSong', NULL, 'Win');
INSERT INTO ChFont VALUES(50, '@FangSong', NULL, 'Win');
INSERT INTO ChFont VALUES(51, 'SimHei', NULL, 'Win');
INSERT INTO ChFont VALUES(52, '@SimHei', NULL, 'Win');
INSERT INTO ChFont VALUES(53, 'KaiTi', NULL, 'Win');
INSERT INTO ChFont VALUES(54, '@KaiTi', NULL, 'Win');
INSERT INTO ChFont VALUES(55, 'DFKai-SB', NULL, 'Win');
INSERT INTO ChFont VALUES(56, '@DFKai-SB', NULL, 'Win');
COMMIT;