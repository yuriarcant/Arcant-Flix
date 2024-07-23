Projeto realizado django

Guia
obs: leia a etapa 22.

1-Ao inicia um projeto com djando , deve ser escrito no terminal:  "django -admin startproject (nome do projeto) ."

2-Para verificar se o site esta funcionando rode no terminal: "python manage.py runserver"

3- para fazer primeiro app no django vamos rodar no terminal um :'django-admin startapp (nome do app) vai criar uma estrutura parecida com a organização do projeto do  flask'

4- vamos rodar 'python manage.py migrate' , ira fazer a atualização do branco de dados

5- toda vez que voce precisar fazer uma atualização no seu site, vamos ter que rodar 2 codigos no terminal: 'python manage.py makemigrations' que cria a estrutura de migração e  o codigo do guia 4 que atualiza o banco de dados.

6- Criar um super usuario que tera acesso total ao site: 'python manage.py createsuperuser' dps de rodar tera q passar um username, email, senha.  o usuario pode ser o msm do email para facilitar.

7- conectar o app (filme) com o seu projeto(arcantflix): vai no seu projeto/ settings e adiciona  o app no INSTALLED_APPS.

8- definir no arquivo urls do projeto(arcantflix) o link que voce quer exibir o  app criado(filme).  vamos criar em cada um dos apps u arquivo urls.py e apontar eles denrto do urls.py do projeto

9- A gora criamos uma class(modelo) no aquivo models chamado Filmes e adicionamos os campos referentes a essa class

10- agora iremos pegar esse modelo e colocar ele no adiminstrativo do nosso site, isso é feito na pasta admin, tbm definimos uma funçao na class filme para exibir o nome do filme no nosso adminstrativo inve de aparece (object 1. etc)

11- vamos configurar no arquivo settings onde vai ficar salva as imagens, static sao imagens que o admin vai sibir para o site(logo, iamgem de botoes etc) e media sao imagens que os usuarios irao postar no seu site.

dentro do urls do seu projeto (arcantflix) voce ira adicionar: '+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)' no urlpatterns e fazer a msm coisa para as medias com :'static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)' mas para a media voce em q definar as variaveis dela no settings . é so seguir o guia que o propio django dara.

obs: ate o momento so conseguimos modificar e ver as coisas atravez do admin do  nosso site. caso tente rodar um runserver agora vai aparecer erro  falando q a pagina nem existe.

12- agora vamos contruir a primeira pagina do nosso site, todas ves que criamos uma pagina, temos que criar 3 coisas: url(link que a pagina vai aparecer), 2 view(codigo em python que vai dizer o que vai acontecer quando entrar naquele link) 3 template(parti vizual ou seja html e css)

13- dentro do urls do app(filmes) vamos criar nossa url(link), essa url vai receber uma views que é uma funçao criada no arquivo views, essa funçao obrigatoriamente vai receber um request.

14- Agora vamos criar um template para nossa home, para poder exibir no link(url) criada acima. dentro do settings podemos ver a variavel templates nela temos APP_DIR:TRUE ou seja um diretorio dentro do seu app(filme) (significa uma pasta dentro do seu app). ou o dirs que é um direotio padrao de todo seu projeto de onde voce vai puxar seus templates.

Exemplo: "DIRS": ['templates'] é criar uma pasta no seu pojeto com o nome que voce passar.

Podemos utiliziar as duas formas, que é o que sera feito no projeto. Onde todas as coisas q englobam de forma geral em nosso projeto (como fonte padrao, uma barra de navegação que serve pra todo site por exemplo), ficara dentro da  pasta template do nosso diretorio geral.
Já as paginas especificas fica no templates de cada app.

Agora denro do app criaremos uma nova pasta que o nome dela "templates" tem que ser exataente esse nome

15- criar a base geral do html do nosso site, no nosso arquivo base, vamos utilizar o bootstrap, ionicons e o tailwind

primeira mente temos q ativar ambos, o bootstrap vamos utilizar para os formularios porque django ja tem uma interação nativa com o bootstrap para os formularios  e o tailwind para resto do site.

O tailwind para ativar basta adicionar o script dentro do head do nosso html base. encontra no site  na aba play cdn, é so copiar

para puxar uma imagem a logo q vai ficar no canto do nosso site ,encontrado no arquivo  do site
E sempre q voce quer utilizar uma imagem q ta dentro do static voce vai comçar com:
{% load static %}
<img src="{% static 'my_app/example.jpg' %}" alt="My image">

16 -  agora falando sobre views, a primeira forma q fizemos foi fbv (function base views) e tem outra forma CBV (class base views), para site simples a fbv é mais pratico, no nosso site vamos utilizar a class. vamos mudar a primeira forma q era.
def homepage(request):
    return render(request, 'homepage.html')

17- agora vamos trabalhar com contex, que é basicamente passar uma informação presente no seu banco de dados para alguma papina do seu sie, isso voce ira passar dentro dafunçao criada para aquele site.

ex: def homefilmes(request):
    context = {}
    lista_filmes= Filme.objects.all()
    context['lista_filmes']= lista_filmes
    return render (request, 'homefilmes.html', context)


aqui fizemos isso apenas para entender de como funciona o fbv (function base views), nos tivemos q puxar a lista e etc, ou seja voce que acaba gerenciando tudo,  já no CBV (class base views) ele fara isso de uma fomra meio automatica.

18- vamos trasformar a nossa essa  fbv (function base views) em CBV (class base views) que vai ser  como vamos utilizar no nosso site.

A primeira mudança a ser realizada para essa migração  no seu views invez de uma funçao voce vai fazer uma class, e importar from django.views.generic import TemplateView, a class ira receber templateview e o seu urls voce tera q importar a class criada e e utilizar ela no link com função as_view()

quando voce quer exibir uma lista, o nome q ficara para ela sera  "object_list". entao no nosso html teremos q fazer a subustituiçao da lista_filmes por object_list.


12- agora criaremos uma view pra cada filme q foi adicionado no site,  dentro do urls vai ter <int:pk> qqque basicamente vai ser o id de cada filme


13- criar links dinamicos no nosso site, no nosso urls do aplicativos vamos dar o parametro name= para o nossos links(path) nesse msm arquivos vamos definir um app_name que vai se utilizado no urls do projeto (arcantflix) como parametro namespace=, agora dentro do html da homefilmes vamos utilizar o filme do nosso projeto, dps puxar o detlhesfilme que para onde eu quero ir e usar o id do filme para saber qual o link.


14- vamos criar nossa classe de episodios e vamos nela utilizar uma chave estrangeira pra sabe de qual filme ela faz referencia, lembrando que é uma boa pratica colocar essa chave estrangeira como sua primeira variavel na sua classe. Podemos fazer essa relaçao de duas formas a 1 serai com ForeignKey que faz uma relaçao de 1 pra muitos e a 2 ManyToManyField que é um arelção de muitos para muitos. o primeiro parametro é o nome da classe(tabela) que ela vai fazer relação, a segunda é related_name= que bsicamento como se criaesse uma tabela com todos os epsisodios referente aquele filme caso voce queira pegar esses episoddios voce buscaria atraves do nome colocado nesse parametro, o terceiro on_delete caso eu delete o filme os episodios tbm seria deletados.

agora o ultimo passo é entrar no nosso arquivo admin e registrar ele igual fizemos com o filme

15- agora vamos colocar na descriçao do filme cada episodio referente aquele filme , para isso vamos mecher no hatml do detalhes filmes, vamos usar o {{ forloop.counter}} para fazer a numeraçao altomatica em cada ep, isso pode ser realizado em qualquer for , tbm vamos fazer ao clicar nos links dos episodios ficar direto e tela cheia, basta pegar  o link EMBAD DDO VIDEO.

16- Agora dentro do detalhes do nosso filme vamos faze uma lista de filme relacionados, para isso vamos criar uma funçao com get_context_data no nosso arquivo views dentro da nossa class de detalhesfilmes , onde o context vai receber nosso detalhes filmes para q rode exatamente como antes . isso permitira passar uma variavel para dentro de uma view espeficica.
agora temos que pegar quais sai os filmes relacionados e os filmes relacionas vao se basear na msm categoria daqele filme em especifico.

agora basta adicionar isso no nosso html de detalhes filmes para ser exibido na nossa pagina.

obs: apenas lembrar q os contexto sao as variaves que voce tem acesso dentro do seu codigo em html

17- vamos criar um context ou  sesja o msm que fizemos acima so que agora ela servira para todas as views do nosso site, criando um novo arquivo python chamado novos_context.dentro desse aquivos para pegar essa infmorçoes vamos definir funçoes onde ela ira retornar uma varaivel q vai ser difinida po nos. no final sempre vamos retornar uma dincionario python cujo a chave do dicionario é o nome da variavel que vai ter no html (que vai ser usada la). isso tudo nos devemos criar.

obs:  dentro da primeira funçao criada na data_criação colocamos  um - , isso serve para por em ordem decrescente

çembrando dps de criar as funçoes nos temos q conectar essas funçoes com o nosso projeto em si, nao basta apenas criar codigos, para isso precisamos ir no nosso settings do nosso projeto, e como estamos mechendo no nosso html vamo configurar isso em nosso templates.

Entao vamos criar um context personalizados no templates, o nossos context ta dentro do app filme, dentro do arquivo novos_context mais o nome do context(função) que voce criou, assim q vamos  ordenar. agora basta colocar essas lista para serem vizualizadas no site . so por no html(homefilmes)

18- agora vamos fazer o sistema de contabilização de vizualizaçoes, mas esse sistema vai ser de forma simplificada, vamos considerar que se alguem clicou na pagina do curso/etc ou seja entrar naos detalhes do filmes vai ser considerado uma vizualização. entao basicamente a view de detalhes do filme vai ser a responsavel em fazer a contagem de vizualização 

No class base views por tras dele ele possui nele ja uma funçao get e uma função post, entao quando o usuario fizer um solicitação do tipo get que no caso e entrar na pagina vamos contar a vizualização, vamos fazer isso no arquivo views do app , na class detalhes filmes .

19- vamos dar uma pausa no codigos em python e vamos trabalhar no html do nosso projeto, na nossos templates homefilmes e detalhesfilmes

20- vamos fazer o filme em destaques exitem duas formas de fazer esse filme em destaque, a 1 dentro da sua views na class home filmes voce poderia pegar um context_data. A 2 que é o que vamos fazer , dentro do novos_context cria uma função que n e necessariamente uma lista(lembrando q tem q adicionar no settings) e dps aplicar no homefilmes.html, o filme em destaque sera o filmes mais novos

22- vamos alterar a barra de navegação com alguns codigos em java script, essas alteraçoes vai servir pra todas as abas do nosso site entao vamos fazer dentro do base.html.

23- agora vamos trabalhar na nossa aba de pesquisa, então primeiro passo vai ser aquelas 3 etapas criar uma view (Pesquisafilme),  criar um template,  e criar um url. a aba de pesquisa ela ta dentro do nossa barra de navegação entao teremos que ir para nossa html da barra e ir na nossa aba de pesquisa que no caso é um formulario, e todo formulario é preciso passar um metodo get ou post e  dps passar o action que é basicamente pra qual link voce quer ser direcionado.

Agora abaixo do nosso formulario vamos criar outro imput do tipe submit (como se fosse um botao que envia informação) e o nosso campo de busca( input acima) teremos q dar um nome para ele.

agora dentro da class (pesquisafilmes) vamos fazer um função q ja é pronta para filtrar nossa pesquisa  , para que o que seja digitado façça as buscas corretamente.

22 - agora vamos fazer a criação de usuarios, entao tbm iremos criar todas as funcionalidades dessa class, agente podderia criar as coisas de usuario em outro app, mas como o site gira em torno dos filmes , vamos criar ele dentro do app(filmes), primeiramente vamos fazer entao nossa classe de usuario, mas teremos que importar a classe padrao no django e dps no settings teremos q mudar algumas coisas para dizer q agora o padrao de usuario nao é mais o do django mas sim do q estamos a construir. para isso iremos ate o settings ate a parte de validaççoes de senhas e passar uma variavel , AUTH_USER_MODEL = "NOME DO APPLICATIVO . CLASS CRIADA", tudo junto
 
Entao criamos a nossa classe Usuario, agora temos que adicionar esse modelo no nosso administrativo e termos que importa uma classe(UserAdmin) nessa etapa porque essa classe usuario é quem vai administrar as coisas do usuario,  como modificamos nossa tabela  temos q fazer as estapas de migrations, mas na hora dessa etapa de migração ira dar um erro pq como a agente ta criando um usuario basicamente novo, basicamente estamos editando o usuario que ja existia desde o começo do projeto, pra esse erro nao acontecer no primeio migrations onde criou nosso banco de dados , nossa tabela etc deveriamos ter dito q esse usuario q acabamos de criar seria o nosso usuario padrao e que ele teria esse novo campo. mas  tem problemas so teremos q resetar essa estrutura. temos 2 formas para isso. partiremos para a primeira pois a segunda nao funcionou nesse porjeto

1- deletar os arquivos na pasta do migrations menos o init e deletar o banco de dados. so que assim voce vai perdei tudo q ja ta dentro do banco de dados, filmes criados , usuario, super-user e etc. dps de deletar so rodar python manage.py makemigrations

lembrando teremos que criar outro super usuario ja q usamos  a opção 1 'python manage.py createsuperuser'

2- ir no settings comentar a:  #AUTH_USER_MODEL = "NOME DO APPLICATIVO . CLASS CRIADA", dps entra no terminal e rodar "python manage.py migrate auth zero"  dps decomentar a linha comentada e rodas python manage.py migrate auth. (essa soluçao nao funcionou para esse projeto)

23- Como optamos pela opçção 1 acima e tivemos que apagar nosso banco dde dados tivemos q adicionar todos os filmes e ep dnv no nosso banco de dados atraves do admin, tbm iremos colocar mais ua seção que é a seção de filme ja visto pelos usuarios afinal a cima trabalhamos para isso.

Então no nosso html do homefilmes temoremos que criar outra seção igual as das lista anteriores(novo/em alta)

24- agora vamos automatizar para que quando um usuario entre em algum filme alem de contabilizar uma vizualização esse filme vara para a lsita de filmes ja vistos, entao dentro d função de contabilizzação iremos fazer esse alteração 


25- agora vamos bloquar a paginas para apenas pessoas logadas utiliziaremos LoginRequiredMixin, que é sempre passado como primeiro parametro dentro das nossa views(class)
alem disso, caso o usuario seja bloqueado de login ele precisa ser redirecionado para algum lugar, no caso seria um lugar de login.

Para isso demos fazer duas configuraçoes no nosso settings, 'LOGIN_REDIRECT_ULR=url/namespace: local para onde  direcionar ele (aqui é pra onde o usuario vai ser redirecionado apos fazer login)   e LOGIN_URL= url/namespace:login  (aqui e a pagina onde o usuario irar fazer login)

agora temos que criar uma ulr para o login, e o seu template , a views nao e necessaria pq o django ja tem esse estrutura pronta, so temos q importa o views, e vamos dar un outro nome para ele pois  views é um nome muito padrao. vamo passar um parametro template_name para ele saber qual templete corresponde a qual

26-vamos  fazer alteraçoes agora na nossa barra de navegação conforme o usuario  esteja  logao ou  não  então vamo mecher diretamente na nosso arquicvo navbar. Posteriormentevamos  tbm faezr o redirecionamento das poaginas caso o  usuario  esteja logado  ele va  direto para a page de filmes.

Entao quando o usuario entra no nosso site ele cai  na pagina homepage, entao nessa class temos que fazer a verificação, para isso vamos fazer novamente a modificação da função get dentro dessa class, entao vamos fazzer isso no nosso arquivo views. (fizemos msm coisa na class detalhes filmes) 

obs: nessa função não podemos fazer um render e redirecionar  para outro template,  nos temos q fazer um redirecionamente para i sso  precisamos importar o  redirect  e dentro  desse url a gente passa a url para onde o usuario vai ser redirecionado igual  nos templates.

27- agora vamos ajeitar os links das nossos botoes para elas ire para cada pagina corretamente , e tbm temoremos q fazer a view((class)) , url , e o template do botao de editar
, essa class ela vai ser um pouco diferente.


28- agora vamos trabalhar um  pouco nos nossos templates, para ajeitar nossas paginas logout e de login, lembrando que quando formos trabalhar com nosso login o djando ja tinha uma views pronta para isso, entao no nosso html de login vamos utilizar uma variavel denominada 'form' denominada automaticamente pelo djando, o form é o formulario. é vamos embelezar esse forulario com o bootstrap que importamos la no incio do projeto no nosso arquivo base. vamos ter q instalar o  'django-crispy-forms' no painel, lembrando que apos a instalação nos temos que por no nossos settings esse novo app no installed_apps. é como estamos utilizando a versao 5 ddo bootstrap vamo tbm instalar o 'crispy-bootstrap5", alem disso temos que instalar duas constantes para esse dois apps.
CRISPY_TEMPLATE_PACK
CRISPY_ALLOWED_TEMPLATE_PACKS

Depois desses passos temos que por o nosso  formulario (form) dettro do template de login,para utilizar o crispy form como referencia, entao no form voce poe '|crispy' e no inicio de toda pagina que voce for utilizar o crispy temos que utilizar  o "{% load crispy_forms_tags %}"

OBS IMPORTANTE: sempre que em algum proeto voce rodar um formulario dentro do seu html que possua um metodo 'POST' , voce obrigatoria mente tem que usar o o 'csrf token', msm coisa que fizemos no projeto flask mais aqui o django ja tem esse toekkn pronto entao so precisa passar a a tag dentro do html.

29- agora vamos criar nossa pagina de criar conta com html e tbm fazer um formulario para ela, para isso iremos criar um novo arquivo chamado forms.py, pq é uma boa praticar colocar  os formualarios personalizados em arquivos separados. dentro desse novo arquivo vamos criar nosssa class  para criar uma conta e dentro dessa class vamos criar outra class denominada Meta que vai me dizer qual modelo que essa class principal vai usar como referencia ou seja se é o modelo padrão do django ou se criamos algum modelo que gerencia nosso usuario e no nosso caso criamos no nosso models a class usuario.

Como estamos criando esse forms persolaziado pq queremos que ele tenha email,  precisamos f azer duas alteraçoes, colocar o campo email, e por segundo editar u campo chamado fields que pe uma tupla com os nomes dos campos q iram aparecer no seu formulario.

agora que criamos o nosso formulario temos que colocar ele na nossa views(class) criarconta ja que ela q exibe a pagina do nosso site alem disso inicialmente criamos essa views como um templateview apanas para ver se ele tava funcionando mais ele agora vai virar um formview e agora precisa passar o form_class , pra isso  vamos ter q dentro do views importa o formulario que acabamos de fazer(Criarcontaform) e tbm o formview 

bom ainda nao terminamos , como no nosso arquivo urls os utilizamos o loginviews ele ja trata diversar coisa( validação de formulario, se foi preeencido corretamente ou nao e etc), é se o formulario estiver certo ele faz o login direto do usuario. e no nosso views(criarconta) quando voce cria um formview, tem duas funççoes que voce precisa editar. a funçao get_success_url que basicamente diz o que vai acontecer se o formulario der certo (essa voce sempre vai por), essa função espera que voce retorne o link para onde o usuario ira ser direcionado entao vamos retorna um reverse(aqui é so o link da pagina) invez do (redirect que retora uma pagina por compelta a pagina toda) entoa pra isso temos q impota o reverse.

obs importante : esse formulario esta criando um item no seu banco de dados n é apenas u formulario que so vai ser analisado e dps descartado entao temos que salvar é isso e feito dentro de uma função form_valid. isso seria a segunda coisa q voce vai ou nao editar, se o formulario nao c riar nada no banco de dados isso nao é necessario fazer

30- forulario da homepage e botao acessar, vamos trazer um formulario que teremos que criar no nosso forms.py para dentro do nosso html homepage e tbm ativar o csrf_token ja que tbm ese formulario é um metodo post, e nossa views da homepage que era um templateview inicialmente vai virar tambem um form views . o formulrio que vamos personalizar pra ca é um formulario padrao do django forms.form.  tbm devemos fazer alteraçoes na funçao get_success_url igual acima . entao vamos pegar o email q foi posto nesse formulario, e vamos verificar se ele ta no banco de dados se tiver ele enviado  para fazer login se nao tiver ele é enviado para criar conta

lembrando poderiamos fazer de diversas maneiras como o nosso botao de  pesquisar , mas vamos fazer dess modo para treinar a crição de um formulario e etc.


31- vamos fazer agora tudo relacionado ao noso botao editar q ue vai ser um novo formulario, podemos fazer um formulario manual feito por nos, mas como o django ja tem isso pronto vamos utiliar  o do django e pra isso vamos importa  no nosso views o updateview, pra isso vamos trocar uma views(class) que esta com nossa pagina de editar perfil (PAGINAPERFIL), inicialmente fizemos ela como um templateviews , dps q fizer a alteração para update view vamos ter q por duas coisa que é o modelo = quem vooce vai q uerer atualizar, que no nosso caso é o nosso usuario e os fields  os campos q agente quer editar no usuario. e tbm teremos q fazer  um get_success_url, lebrando q temos q colocar no nosso arquivo url no path de editar perfil a chave primaria que nada mais é do que o id, para poder redirecionar de maneira correta e tbm editar corretamente aquele usuario. alem disso no nosso navbar  , o botao de editar perfil agora tbm ira precisar da variavel do id do usuario 

lembrando os nomes dos fields(campos) que querewmos editar corresponde a nossa class usuario que usa o AbstractUser , posso olhar esses campos abrindo o nosso banco de dados.

32- agora vamos criar  o mudar senha, que é a msm coisa q o nosso editar perfil é extamente a msm pagina ,isso é importante pq como é exatamente a msm pagina no nosso urls nos vamos reaproveitar esse html no casso editarperfil.html  para o mudarsenha, so que o fields sao o de mudar a senha confirmação de senha e etc, mas vamos fazer isso atraves de um auth_view com auth_views.PasswordChangeView.as_view() e passando qual é o tempalte dele
.

FIM PROJETO E GUIA.

Agora o que deveriamos fazer é o deploy do nosso projeto em algum servidor.  vou por um guia de como colocar esse projeto no git hub e talvez um guia para por no servidor do railway que no momento é gratuito.

COLOCANDO O PROJETO NO GIT HUB (necesari oter o git isntalado pc etc)

abra o terinal rode o - git init
depois rode um - dit add . (o ponto que ddizer todos os arquivos)