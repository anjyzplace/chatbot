FROM mongo

COPY . .

# RUN mongoimport --db microsoftbotframework --collection healthdata --type csv --headerline --file /data/newhealthdata.csv
RUN ls

CMD mongod --dbpath /data/db --fork --syslog \
&& mongoimport --host database --db microsoftbotframework --collection healthdata --type csv --headerline --file ./data/newhealthdata.csv \
&& mongoimport --host database --db microsoftbotframework --collection exercise --type csv --headerline --file ./data/exercise.csv \
&& mongoimport --host database --db microsoftbotframework --collection food --type csv --headerline --file ./data/food.csv \
&& mongoimport --host database --db microsoftbotframework --collection drinks --type csv --headerline --file ./data/drinks.csv \