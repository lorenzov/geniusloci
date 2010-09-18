# Replace these three settings.
PROJDIR="/home/ubuntu/geniusloci/src/geniusloci"
PIDFILE="$PROJDIR/mysite.pid"
SOCKET="/home/ubuntu/geniusloci.sock"
export PYTHONPATH=/home/ubuntu/geniusloci/src/:/var/django/
export DJANGO_SETTINGS_MODULE=geniusloci.settings
cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

exec ./manage.py runfcgi  method=threaded host=127.0.0.1 port=3034 pidfile=$PIDFILE
