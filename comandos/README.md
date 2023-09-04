Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate
Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME

python manage.py shell abre um terminal interativo do django, nesse terminal é possivel realizar diversas coisas, como por exemplo inserir na base de dados um dado, para o exemplo do projeto agenda, podemos
utilizar a seguinte sintaxe:

python manage.py shell:

	>> from contact.models import Contact
	>> Contact -- Para ver se funcionou
	>> c = Contact(campo que deseja inserir, exemplo: first_name="teste")
	>> c.save() -- Adiciona na base de dados
	>> c.delete() -- para deletar o dado da base de dados. Entretanto é valido destacar que por mais que seja apagado do banco de dados o dado, ele ainda existira na memoria, ou seja é possivel inserir aquele dado
	novamente apenas utilizando c.save()
	>> para fazer alguma alteração, por exemplo alterar o numero de telefone, basta c.campo = novo_valor

	metodo get -- Usado para retornar um unico dado da base de dados, ou seja se voce utilizar esse metodo e ele encontrar mais que um ou menos que um dado ele retornará erro, 
	sintaxe: c = Contact.objects.get(campo, exemplo 'id'=4)
	essa consulta retornará um valor
	É um jeito útil de você alterar os valores da base de dados
	
	Metodo all - Retorna todos os valores da base de dados em formato de query Set, varios valores em um conjunto. Sintaxe: c = Contact.objects.all()
	
	# Importe o módulo
	from contact.models import Contact
	# Cria um contato (Lazy)
	# Retorna o contato
	contact = Contact(**fields)
	contact.save()
	# Cria um contato (Não lazy)
	# Retorna o contato
	contact = Contact.objects.create(**fields)
	# Seleciona um contato com id 10
	# Retorna o contato
	contact = Contact.objects.get(pk=10)
	# Edita um contato
	# Retorna o contato
	contact.field_name1 = 'Novo valor 1'
	contact.field_name2 = 'Novo valor 2'
	contact.save()
	# Apaga um contato
	# Depende da base de dados, geralmente retorna o número
	# de valores manipulados na base de dados
	contact.delete()
	# Seleciona todos os contatos ordenando por id DESC
	# Retorna QuerySet[]
	contacts = Contact.objects.all().order_by('-id')
	# Seleciona contatos usando filtros
	# Retorna QuerySet[]
	contacts = Contact.objects.filter(**filters).order_by('-id')
	