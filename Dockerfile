FROM python

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD [ "gunicorn","--bind","0.0.0.0:8000","AuctionPlatform.wsgi:application" ]