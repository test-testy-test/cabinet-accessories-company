SELECT *
FROM dbo.Data$
ORDER BY date_of_sale ASC;

--Add sales_revenue col 
ALTER TABLE dbo.Data$
ADD sales_revenue MONEY NULL;

UPDATE dbo.Data$ SET sales_revenue = list_price * quantity_sold;

--Add total_cost col
ALTER TABLE dbo.Data$
ADD total_cost MONEY NULL;

UPDATE dbo.Data$ SET total_cost = cost * quantity_sold;

--Add gross_profit col
ALTER TABLE dbo.Data$
ADD gross_profit MONEY NULL;

UPDATE dbo.Data$ SET gross_profit = sales_revenue - total_cost;

--Create table displaying total sales revenue by region for each of the four years and quarters
ALTER TABLE dbo.Data$
ALTER COLUMN date_of_sale DATETIME;

ALTER TABLE dbo.Data$
ADD Year_Quarter AS (CASE  
                        WHEN MONTH(date_of_sale) BETWEEN 01 AND 03 THEN convert(char(4), YEAR(date_of_sale)) + '-Q1'
						WHEN MONTH(date_of_sale) BETWEEN 04 AND 06 THEN convert(char(4), YEAR(date_of_sale)) + '-Q2'
						WHEN MONTH(date_of_sale) BETWEEN 07 AND 09 THEN convert(char(4), YEAR(date_of_sale)) + '-Q3'
						WHEN MONTH(date_of_sale) BETWEEN 10 AND 12 THEN convert(char(4), YEAR(date_of_sale)) + '-Q4'
                    END);

--TABLE 1
SELECT 
	SUM(sales_revenue) AS total_sales_revenue,
	region,
	Year_Quarter
FROM dbo.Data$
GROUP BY region, Year_Quarter
ORDER BY Year_Quarter, region;

--Create a table displaying sales revenue, total cost, and gross profit for each year
ALTER TABLE dbo.Data$
ADD Year AS (CASE  
                 WHEN MONTH(date_of_sale) BETWEEN 01 AND 03 THEN convert(char(4), YEAR(date_of_sale)) 
				 WHEN MONTH(date_of_sale) BETWEEN 04 AND 06 THEN convert(char(4), YEAR(date_of_sale))
				 WHEN MONTH(date_of_sale) BETWEEN 07 AND 09 THEN convert(char(4), YEAR(date_of_sale))
				 WHEN MONTH(date_of_sale) BETWEEN 10 AND 12 THEN convert(char(4), YEAR(date_of_sale)) 
             END);

--TABLE 2
SELECT 
	SUM(sales_revenue) AS total_sales_revenue,
	SUM(total_cost) AS total_cost,
	SUM(gross_profit) AS gross_profit,
	Year
FROM dbo.Data$
GROUP BY Year;

--Find most profitable brand for each year (measured by gross profit)
SELECT 
	DISTINCT Year, 
	brand,
	MAX(gross_profit) AS gross_profit
FROM dbo.Data$
GROUP BY brand, Year
ORDER BY YEAR ASC;

--TABLE 3
WITH DATA AS 
(SELECT
	"Year", 
	brand,
	gross_profit,
	dense_rank() OVER (PARTITION BY "Year" ORDER BY gross_profit DESC) AS dr
FROM dbo.Data$) 
SELECT * FROM DATA WHERE dr = 1 
ORDER BY "Year";

--For 2018, by brand, sort collection by gross profit percentage
WITH agg AS
(
  SELECT DISTINCT
    brand,
    collection,
    gross_profit,
    SUM(gross_profit) OVER (PARTITION BY brand, collection) 
      AS collection_gross_profit_total,
    SUM(gross_profit) OVER (PARTITION BY brand) 
      AS brand_gross_profit_total
  FROM dbo.Data$    
  WHERE Year='2018'
  GROUP BY brand, collection, gross_profit
)
SELECT brand, collection, gross_profit, 
   collection_gross_profit_total,
   brand_gross_profit_total,
   ((collection_gross_profit_total / brand_gross_profit_total) * 100) 
     AS gross_profit_percentage 
FROM agg;

--Create table to place TABLE 4 values in
CREATE TABLE collection_gross_profit_percentage (
brand varchar(10),
collection varchar(10),
gross_profit_percentage DECIMAL(5,2),
Year INT);

--Insert values into collection gross profit percentage table
INSERT INTO collection_gross_profit_percentage (brand, 
collection, gross_profit_percentage, Year) VALUES
('Elements','Aiden',-2.04, 2018),
('Elements','Arcadia',1.40, 2018),
('Elements','Asher',3.00, 2018),
('Elements','Belfast',3.07, 2018),
('Elements','Brenton',4.49, 2018),
('Elements','Calloway',3.33, 2018),
('Elements','Capri',1.08, 2018),
('Elements','Cosgrove',2.46, 2018),
('Elements','Cypress',0.54, 2018),
('Elements','Drake',1.77, 2018),
('Elements','Edgefield',4.58, 2018),
('Elements','Florence',1.54, 2018),
('Elements','Gatsby',2.13, 2018),
('Elements','Geneva',1.20, 2018),
('Elements','Glendale',1.52, 2018),
('Elements','Hadley',0.52, 2018),
('Elements','Hadly',0.96, 2018),
('Elements','Hammond',0.68, 2018),
('Elements','Kenner',0.91, 2018),
('Elements','Kingsport',0.83, 2018),
('Elements','Lindos',2.30, 2018),
('Elements','Luxe',0.48, 2018),
('Elements','Madison',26.97, 2018),
('Elements','Merryville',0.79, 2018),
('Elements','Naples',9.67, 2018),
('Elements','Palisade',0.33, 2018),
('Elements','Park',1.54, 2018),
('Elements','Palisale',0.10, 2018),
('Elements','Seaver',1.26, 2018),
('Elements','Sedona',0.65, 2018),
('Elements','Slade',2.60, 2018),
('Elements','Somerset',1.53, 2018),
('Elements','Stanton',5.96, 2018),
('Elements','Strickland',2.41, 2018),
('Elements','Syracuse',0.75, 2018),
('Elements','Tempo',0.48, 2018),
('Elements','Torino',1.94, 2018),
('Elements','Verona',1.98, 2018),
('Elements','Vienna',0.68, 2018),
('Elements','Watervale',0.86, 2018),
('Elements','Westbury',0.66, 2018),
('Elements','Zachary',1.90, 2018),
('Jeffrey','Aberdeen',1.12, 2018),
('Jeffrey','Alvar',0.47, 2018),
('Jeffrey','Amsden',0.61, 2018),
('Jeffrey','Annadale',1.15, 2018),
('Jeffrey','Anwick',1.65, 2018),
('Jeffrey','Backplates',0.63, 2018),
('Jeffrey','Belcastel',8.17, 2018),
('Jeffrey','Bella',2.63, 2018),
('Jeffrey','Bienville',0.13, 2018),
('Jeffrey','Bordeaux',0.36, 2018),
('Jeffrey','Breighton',0.58, 2018),
('Jeffrey','Bremen',6.91, 2018),
('Jeffrey','Cairo',0.25, 2018),
('Jeffrey','Caille',0.60, 2018),
('Jeffrey','Chesapeake',2.12, 2018),
('Jeffrey','Cordova',2.12, 2018),
('Jeffrey','Delgado',5.08, 2018),
('Jeffrey','Delmar',2.89, 2018),
('Jeffrey','Durham',3.08, 2018),
('Jeffrey','Duval',2.98, 2018),
('Jeffrey','Ella',2.64, 2018),
('Jeffrey','Encada',0.48, 2018),
('Jeffrey','Evangeline',0.22, 2018),
('Jeffrey','Glenmore',2.15, 2018),
('Jeffrey','Grande',0.58, 2018),
('Jeffrey','Harlow',1.48, 2018),
('Jeffrey','Hayworth',1.04, 2018),
('Jeffrey','Hudson',1.37, 2018),
('Jeffrey','Katharine',0.47, 2018),
('Jeffrey','Kensington',0.29, 2018),
('Jeffrey','Key Largo',0.09, 2018),
('Jeffrey','Lafayette',1.40, 2018),
('Jeffrey','Latches',0.11, 2018),
('Jeffrey','Lenoir',0.20, 2018),
('Jeffrey','Lexa',1.02, 2018),
('Jeffrey','Leyton',1.06, 2018),
('Jeffrey','Lille',2.27, 2018),
('Jeffrey','Lyon',0.40, 2018),
('Jeffrey','Marlo',2.75, 2018),
('Jeffrey','Maybeck',1.71, 2018),
('Jeffrey','Milan',4.84, 2018),
('Jeffrey','Mirada',0.69, 2018),
('Jeffrey','Modena',1.48, 2018),
('Jeffrey','Montclair',2.48, 2018),
('Jeffrey','Odessa',0.32, 2018),
('Jeffrey','Padua',0.21, 2018),
('Jeffrey','Prestige',3.68, 2018),
('Jeffrey','Rae',6.01, 2018),
('Jeffrey','Regan',0.18, 2018),
('Jeffrey','Regency',0.40, 2018),
('Jeffrey','Rhodes',1.65, 2018),
('Jeffrey','Rochester',-0.24, 2018),
('Jeffrey','Royce',0.27, 2018),
('Jeffrey','Solana',0.44, 2018),
('Jeffrey','Sonoma',1.47, 2018),
('Jeffrey','Sutton',1.11, 2018),
('Jeffrey','Symphony',0.34, 2018),
('Jeffrey','Tahoe',1.69, 2018),
('Jeffrey','Tiffany',2.67, 2018),
('Jeffrey','Tuscany',0.69, 2018),
('Jeffrey','Valencia',0.20, 2018),
('Jeffrey','Venezia',0.26, 2018),
('Jeffrey','West',0.40, 2018),
('Jeffrey','Zane',1.57, 2018),
('Jeffrey','Zurich',0.49, 2018);

--TABLE 4
SELECT *
FROM collection_gross_profit_percentage
GROUP BY brand, collection, gross_profit_percentage, Year
ORDER BY brand, gross_profit_percentage DESC;

--Find most profitable region by gross profit percentage
SELECT
	SUM(gross_profit) 
FROM dbo.Data$
WHERE Year='2018';
--Output: 60366184.929

--TABLE 5
SELECT 
	DISTINCT region, 
	((SUM(gross_profit) / 60366184.929) * 100) AS gross_profit_percentage,
	SUM(gross_profit) AS gross_profit_total
FROM dbo.Data$ 
WHERE Year='2018'
GROUP BY region
ORDER BY gross_profit_percentage DESC;
