# FIEK-Protokolli
## Programimi me soketa me TCP dhe UDP 
Protokolli FIEK është një protokoll shumë i thjeshtë që i lejon klientit dhe serverit ti testoj lidhjet e tyre. Ky nuk
është një protokoll standard. Është TCP versioni i cili quhet FIEK-TCP dhe UDP versioni i cili quhet FIEK-UDP.
Protokolli FIEK përmban këto kërkesa (metoda): IP, NRPORT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA,
KONVERTO dhe GCF te cilat mund te dërgohen nga klienti tek serveri. Serveri përgjigjet me një mesazh i cili është
specifik për secilën kërkesë (metode). Serveri i injoron kërkesat jovalide dhe nuk duhet dështon në rast
se pranon një kërkesë te tillë.
### FIEK-TCP
Për të bërë një kërkesë, klienti FIEK-TCP se pari vendos një lidhje TCP me FIEK-TCP serverin.
Klienti pastaj e dërgon kërkesën te serveri dhe nëse kërkesa është valide, serveri pastaj e kthen përgjigjen dhe
vazhdon punën për ndonjë komand të re që mund ti kërkohet nga klientët tjerë.
### FIEK-UDP 
Për te bere një kërkesë, klienti FIEK-UDP dërgon kërkesën vetëm nëpërmjet një UDP
datagrami për tek FIEK-UDP serveri. Nëse kërkesa është valide, serveri pastaj e kthen përgjigjen ne një UDP
datagram. Vetëm një kërkesë mund te dërgohet për datagram.
#### Serveri
Programi Server është dizajnuar që të punoj vazhdimisht pa ndërprerje (përveç rasteve kur ndodh ndonjë
gabim). Serveri është në gjendje që të pranoj një sekuencë te kërkesave nga i njëjti klient apo nga klient. Për ta arritur këtë implementimi është bërë përmes Thread-ave.
#### Klienti
Klienti është në gjendje të thërras kërkesat dhe të merr përgjigjie nga serveri. 

### Veglat e përdorura
* Python 3.6
* Visual Studio 2015
* Librari të gatshme në Python 

### Kontribuesit 
[BlertaMecini](https://github.com/BlertaMecini)
<a href="https://github.com/BlertaMecini/FIEK-protokolli/graphs/contributors">
<img src="https://contrib.rocks/image?repo=FIEK-protokolli/INT20_21_Gr16">
</a>
### Licensa 
Ky projekt është i licensuar nën licensën MIT - shikoni skedarin [LICENSE.md](https://github.com/BlertaMecini/FIEK-Protokolli/blob/main/LICENSE) për detaje.
