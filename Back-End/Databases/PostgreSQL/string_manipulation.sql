--- clean up like Chinese (Simplified) / 简体中文 to Chinase
-- 1) Split if to get Chinese (Simplified)
-- 2) Split to get 'Chinase '
select id, SPLIT_PART(SPLIT_PART(name, '/', 1), '(', 1) from res_lang;
select id, TRIM(BOTH ' ' FROM SPLIT_PART(SPLIT_PART(name, '/', 1), '(', 1)) from res_lang;
select id, TRIM(SPLIT_PART(SPLIT_PART(name, '/', 1), '(', 1)) AS name from res_lang;
select id, LOWER(TRIM(SPLIT_PART(SPLIT_PART(name, '/', 1), '(', 1))) AS name from res_lang;

SELECT 
    id, 
    LOWER(
        TRIM(
            SPLIT_PART(
                SPLIT_PART(
                    name, -- like Chinese (Simplified) / 简体中文
                    '/', 1
                )
                '(', 1
            )
        )
    ) AS name
FROM 
    res_lang;