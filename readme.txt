Script, der sletter userdata og userthemes fra SPS.

- Lavet til MSSQL-databaser.
- Bat-filen er lavet til den i ArcGIS Pro medfølgende python.exe. 

Tilretning:
- Scriptet skal tilrettes så variablen userids kommer til at indeholde de brugerid, der skal have slettet deres data. Dette afhænger af hvordan I får fat i disse.
- Udfyld config.json med credentials. 
	- Hvis du logger på databasen med AD i stedet for user/pwd, skal credentials.uid og credentials.pwd slettes og erstattes af "trustedconnection":"yes"
- config.credentials indeholder også navnet på driveren til MSSQL-databasen. dette er versionsafhængigt (databaseversion).


LÆS SCRIPTET OG DETS SQL-FORESPØRGSLER IGENNEM INDEN ANVENDELSE.
SCRIPTET FORETAGER IRREVERSIBLE SLETNINGER I DATABASEN. JEG FRALÆGGER MIG ETHVERT ANSVAR.

mon13@esbjerg.dk
