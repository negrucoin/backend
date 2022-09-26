function run(){
  docker-compose -f docker-compose.preflight.yml "$@"
}
set -e
run build web
run run web sh /docker/ci.sh
run down --volumes
