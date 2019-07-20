#TODO IMPLEMENT
# Enter your name here
mhs_name = 'Ridwan' # TODO Implement this
def index(request):
response = {'name': mhs_name}
return render(request, index_lab1.html, response)
