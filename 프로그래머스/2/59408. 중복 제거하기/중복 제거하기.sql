# select (case when NAME IS NULL then 0 else 1 end) count
# # select count(NAME)
# from ANIMAL_INS 
# group by NAME


# select sum(NAME) 
# from ANIMAL_INS 
# group by NAME
# having count(NAME) 

SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL