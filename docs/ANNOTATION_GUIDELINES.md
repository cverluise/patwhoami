# ANNOTATION GUIDELINES

## Variables

name | description | type
---|---|---
text    | The name (lower-cased) of the entity | `str`
cat     | The category of the entity. `"RES_INSTITUTE"` for research institute/agency, `"UNIVERSITY"` for university/graduate schools, `"HOSPITAL"` for hospitals and `"OTHER"` for others (non research agents, incl. people and companies)| `int`
country\_code    | The country code of the main country of the entity | `str`

## Sources


country\_code   | University/graduate school | Research institute/agency | Hospital | Other
---|---|---|---|---
US JP DE KR CN FR GB TW CH IT SU NL SE CA ES   |  [Lists of universities and colleges by country](https://en.wikipedia.org/wiki/Category:Lists_of_universities_and_colleges_by_country)    |  [Lists of research institutes by country](https://en.wikipedia.org/wiki/Category:Research_institutes_by_country)    |  [Lists of hospitals by country](https://en.wikipedia.org/wiki/Category:Lists_of_hospitals_by_country)    |  [Lists of companies by country](https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country) [List of Nobel laureates by country](https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country)

We complete our list with other data (or remplace wiki data when the title is tagged with * symbol):

country\_code | source
---|---
DE  | [CIO list of top 500 companies](https://www.cio.de/top500)
FR  | [univ-ag list of main higher education](http://www1.univ-ag.fr/aoc/liens/organismes.html) | [Wiki Liste des Etablissements publics à caractères scientifique*](https://fr.wikipedia.org/wiki/Liste_des_%C3%A9tablissements_publics_%C3%A0_caract%C3%A8re_scientifique,_culturel_et_professionnel)  [List of registered companies*](https://www.data.gouv.fr/fr/datasets/entreprises-immatriculees-en-2017)
US  | [Alumni by university or college in the United States by state](https://en.wikipedia.org/wiki/Category:Alumni_by_university_or_college_in_the_United_States_by_state)
CN  | [List of members of the Chinese Academy of Sciences](https://en.wikipedia.org/wiki/Category:Members_of_the_Chinese_Academy_of_Sciences )
CH  | [List of institutes associated with CERN](https://en.wikipedia.org/wiki/Category:CERN)
CA  | [List of National Research Council institutes](https://en.wikipedia.org/wiki/Category:National_Research_Council_(Canada)) [Medical research institutes in Canada](https://en.wikipedia.org/wiki/Category:Medical_research_institutes_in_Canada) [Military research installations of Canada](https://en.wikipedia.org/wiki/Category:Military_research_installations_of_Canada) [Defence Research and Development Canada](https://en.wikipedia.org/wiki/Category:Defence_Research_and_Development_Canada)
SU  | [Institutes of the Russian Academy of Sciences](https://en.wikipedia.org/wiki/Category:Institutes_of_the_Russian_Academy_of_Sciences) [Nuclear research institutes in Russia](https://en.wikipedia.org/wiki/Category:Nuclear_research_institutes_in_Russia)
ES  | [Research institutes in Andalusia](https://en.wikipedia.org/wiki/Category:Research_institutes_in_Andalusia) [Research institutes in the Basque Country](https://en.wikipedia.org/wiki/Category:Research_institutes_in_the_Basque_Country_(autonomous_community)) [Research institutes in Catalonia](https://en.wikipedia.org/wiki/Category:Research_institutes_in_Catalonia) [Research institutes in Galicia in Spain](https://en.wikipedia.org/wiki/Category:Research_institutes_in_Galicia,_Spain) [Research institutes in the Community of Madrid](https://en.wikipedia.org/wiki/Category:Research_institutes_in_the_Community_of_Madrid) [Medical research institutes in Spain](https://en.wikipedia.org/wiki/Category:Medical_research_institutes_in_Spain) [Neuroscience research centers in Spain](https://en.wikipedia.org/wiki/Category:Neuroscience_research_centers_in_Spain) [Think tanks based in Spain](https://en.wikipedia.org/wiki/Category:Think_tanks_based_in_Spain)

!!! note
    In order to keep the training data balanced, we had to sample some lists:

    - FR Other: random sample - 600
    - US Hospitals: restrict to Colorado, Florida and Minnesota
    - US Other: Restrict to Alabama, Hawai, Indiana, Iowa, Missouri, New-Jersey, Ohio, Virginia, Wisconsin
    - GB Other: Sample Companies

    For korean list I use both South and North Korea data, for China we use both China and Hong Kong data and we use Russian data instead of USSR data.


## Training sample

| country\_code  |   HOSPITAL |   OTHER |   RES\_INSTITUTE|   UNIVERSITY |
|:---------------|-----------:|--------:|----------------:|-------------:|
| CA             |        219 |     538 |             126 |           96 |
| CH             |         58 |     266 |              81 |           72 |
| CN             |        223 |     750 |              61 |          181 |
| DE             |         79 |     821 |             105 |          427 |
| ES             |        214 |     123 |              72 |           88 |
| FR             |        124 |     770 |              53 |          147 |
| GB             |        771 |     895 |              67 |          264 |
| IT             |         88 |     401 |              52 |          109 |
| JP             |        303 |     768 |              53 |          947 |
| KR             |         56 |     411 |              36 |          514 |
| NL             |        131 |     132 |              68 |           95 |
| SE             |        103 |     336 |              41 |           55 |
| SU             |         28 |     220 |             162 |          634 |
| TW             |         64 |     221 |              24 |          163 |
| US             |        612 |    1067 |             295 |         2511 |
