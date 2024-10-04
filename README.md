# P&O 3: eKubb

## Git installeren
Om Github efficient te gebruiken is het belangrijk om Git te installeren. Voor diegenen met [Winget](https://github.com/microsoft/winget-cli) is het makkelijk: `winget install --id Git.Git -e --source winget`. Als je geen package manager hebt kun je het ook altijd installeren vanop de [Git website](https://git-scm.com/download/win)


### Basic terminal commands
1. `ls` zal alle files tonen die in de directory (map) zitten waar je in aan het werken bent.
2. Om van directory te veranderen gebruik je best: `cd <directory name>`. Sommige terminals zijn hoofdlettergevoelig sommige niet.
3. Een directory teruggaan doe je met `cd ..`, naar de home directory gaat sneller met `cd ~`.
4. Een nieuwe directory maken kan met: `mkdir <directory name>`
5. Een lege verwijderen met: `rm -d <directory name>`
6. Een niet lege kan met: `rm -r <directory name>`. Het kan zijn dat hij promt of je zeker bent of je de files wilt deleten. Als je zeker bent typ je `y` en druk dan op enter.
7. Om ervoor te zorgen dat hij die promts niet geeft kan je `rm -rf <directory name>` gebruiken.
>[!NOTE]
>Bij Windows command prompt (cmd) zijn sommige commands anders, maar normaal staat op elk windows systeem wel een powershell dus je kan altijd die gebruiken of de git terminal die bij een git installatie zit natuurlijk.


### Git commands
Om te werken in een Github repository moet je die eerst lokaal klonen. Navigeer met de terminal naar een map waar je deze kloon wilt maken en doe daar het commande: `git init`.
1. `git clone https://github.com/CasparSalaets/PnO2`
2. Vervolgens moeten we een remote instellen, dit gaat met: `git remote add origin https://github.com/CasparSalaets/eKubb.git`
3. Om verdere updates lokaal door te voeren doe je: `git pull origin <branch name>`, om alles te updaten voer je bij branch name `main` in.
Dit zal deze repository klonen naar jouw harde schijf zodat je er makkelijk aanpassingen aan kan maken. Het kan zijn dat je moet inloggen met github in de terminal omdat deze repository niet publiek is. Hiervoor zijn wel [Github Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) voor nodig (niet in git bash). Ik zal dat wel eens voordoen als dat nodig is.

Nadat de aanpassingen gemaakt zijn is het tijd om de veranderingen door te geven aan de repository. Dit gebeurt met de volgende git commands.

Vooraleer we de aanpassingen definief doorvoeren naar de branch `main`, zullen we ze in een apparte stoppen. Op dit moment zijn er al twee branches gemaak, nl. `updates_Thor` en `updates_Caspar`. Branches hebben het voordeel dat je aanpassingen ergens appart worden opgeslagen voordat ze definief worden door branches te 'mergen'.
Als je de repository gekloont heb zal je automatisch in de branch `main` zitten. Om te veranderen typ je: `git checkout <branch name>`, hiervoor moet de branch al wel bestaan.
Om een branch te maken doe je: `git branch <branch name>`. Vervolgens moet je de branch naar Github pushen met `git push origin <branch name>`. Om een lijst van alle branches te krijgen doe je: `git branch -a`


1. Eerst voegen we de geupdate file toe aan de 'staging area'. Hier zullen alle files komen die we aangepast hebben. Elke file moet appart worden toegevoegd. Dit gebeurd met `git add <filename>`.
1. Een optionele commando is: `git status`. Dit commando laat zien welke files er in de stagin area zitten en hoeveel aanpassingen er gebeurd zijn.
2. Vervolgens moeten we de file 'committen': `git commit -m "<text message>`" en voeg hierbij een korte beschrijving toe van wat er aangepast is. Als er fouten zouden instaan is het altijd makkelijk om de veranderingen om te draaien. Zonder deftige beschrijving is dat al een pak lastiger.
4. Ten laatste moeten we het nog 'doorpushen' naar Github zelf. Dit gebeurd met het commando: `git push -u origin <branch name>` Hier zal je zeker moeten inloggen omdat niet iedereen in elke repository editing rights heeft. Ook hierweer moet je ipv je wachtwoord een token gebruiken.
5. Als alles definitief is en werkt zullen we de branches mergen met main om zo tot een stabiele versie te komen.
