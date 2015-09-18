RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

function echo_info {
    echo -ne "${GREEN}${1}${NC}"
}

function echo_status {
    echo -e "${RED}${1}${NC}"
}

export PYTHONPATH=`pwd`

echo_info "Getting existing Django version..."
existing_version=`pip freeze | grep -i Django=`
echo_status "DONE"

echo_info "Uninstalling $existing_version..."
pip uninstall -yq Django
echo_status "DONE"

echo_info "Installing Django 1.6..."
pip install -q "Django<1.7"
echo_status "DONE"

echo_status "Running migrations using South..."
django-admin.py schemamigration --auto django_condition_chain --settings=settings.dev_south

echo_info "Uninstalling Django 1.6..."
pip uninstall -yq Django
echo_status "DONE"

echo_info "Installing latest Django..."
pip install -q Django
echo_status "DONE"

echo_status "Running migrations using latest Django..."
django-admin.py makemigrations django_condition_chain --settings=settings.dev

echo_info "Uninstalling latest Django..."
pip uninstall -yq Django
echo_status "DONE"

echo_info "Reinstalling $existing_version..."
pip install -q $existing_version
echo_status "DONE"
