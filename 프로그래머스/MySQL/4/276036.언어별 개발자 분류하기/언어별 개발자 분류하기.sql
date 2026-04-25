WITH RECURSIVE Combinations AS (
    -- 1. Anchor Member: 1개짜리 조합 생성
    SELECT 
        CODE, -- 조합의 최소 코드 값부터
        (Name = 'C#') as has_Csharp,
        (Name = 'Python') as has_Python,
        (Category = 'Front End') as has_FE,
        CODE AS skill_code
    FROM SKILLCODES 

    UNION ALL

    -- 2. Recursive Member: 기존 조합에 새로운 행 추가
    SELECT 
        sk.CODE,
        (c.has_Csharp OR (sk.Name = 'C#')) AS has_Csharp,
        (c.has_Python OR (sk.Name = 'Python'))as has_Python,
        (c.has_FE OR (Category = 'Front End')) as has_FE,
        skill_code + sk.CODE AS skill_code
    FROM Combinations c
    INNER JOIN SKILLCODES sk ON c.CODE < sk.CODE  -- 중복 방지 및 순서 보장을 위한 핵심 조건
), 
grades as (
    -- Front 이면서 Python이 있으면 A / python 없으며 C# 있으면 B 아니면 C
    -- 그리고 C#이 있으면 B, 아니면 일단 null(이게 있을까?)
    select
        if(has_FE, if(has_Python, 'A', 
                                    if(has_Csharp, 'B', 'C')
                     ),
                    if(has_Csharp, 'B', null)
          )
            as grade,
        skill_code
    from Combinations
)
select g.grade,
    d.ID, d.Email
from developers as d
    left join grades g
        on d.skill_code = g.skill_code
where grade is not null
order by grade, ID