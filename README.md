# question-answer-hitalent

Для запуска проекта достаточно ввести команду docker-compose up
Если вы хотите использовать локальную базу данных, то можно поменять строку подключения в docker-compose DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/hitalent
Так же она указывается в database.py и migrations.env.py 

