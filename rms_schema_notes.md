# resume management system schema

## requirement questions

- In the use case 1, is the format itself data? Should we store the format data in the database? Or the formats are static/hardcoded in the frontend?

- In the use case 2, does it mean that the head hunter will need to find candidates who have had work experience in the same company for more than 5 years? Just to double-check if I'm getting it right.

## assumption

- a small system, not for C10K/distributed case
- int auto-increment as PK is not suitable for distributed system case(maybe need to merge data in the future?)
- In the use case 2, if there are huge amount of work experience records, there will be a full table scan performance issue. Will need to add an index on start column for computing the timeframe between start time and now. Will need a column to store pre-computed year of experience and add an index.
- address could be seperated to different columns if needed
- created/updated column could be added to every table for auditing
