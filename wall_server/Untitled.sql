
#原始数据记录
CREATE TABLE wallRecord(
id bigint(20) primary key NOT NULL AUTO_INCREMENT, 
wallName varchar(255),
appName varchar(255),
cost float,
taskNumLeft int,
updatetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

select * from wallRecord;


insert into wallRecord (wallName, appName,cost,taskNumLeft) 
VALUES ("小鱼赚钱","安居客",1.2,1000);

