# Py Docx to HTML using mammoth

This script was made for a specific buisness requirment of a project on which I am working at the moment of it's creation. The task was to create a static HTML version of privacy policies so that they could be loaded on the client's website. This client had several brand under it and they wanted one HTML page for every brand containing all the privacy informative. The privacy informative is divided into countries and every country may have one or more version of privacy notice in different languages, for example, Brand X has: Austria with en and de, US with en only, Italy with it and en versions. 

## Input of the script

At every run, the script will look for folders in 'InputDocx' folder which will contain all the input dataset.

The legal office of the company passes one folder for every country containing the docx file or files. So the structure of the given files is as following:

**Brand X (folder):**
 - Country 1 (folder):
   - Language 1 (docx)
   - Language 2 (docx)
   - ...
 - Country 2 (folder):
   - Language 1 (docx)
   - Language 2 (docx)
   - ...
 - Country n ...

**Brand Y (folder):**
 - Country 1 (folder):
   - Language 1 (docx)
   - Language 2 (docx)
   - ...
 - Country 2 (folder):
   - Language 1 (docx)
   - Language 2 (docx)
   - ...
 - Country n ...

**Brand ...**

***IMPORTANT***

The script input files must be formatted correctly, otherwise the result may be unexpected. 
- Be sure every Brand folder is named correctly
- Be sure every country is named correctly (e.g. 'Austria' is correct, 'Austria International' is not correct)
- Be sure every docx file has just one version per language and the naming convention of the file is followed:
 >  [LANGUAGE].docx 

## Expected output of the script

The main purpose of the script is to generate one HTML doc for every brand containing every country for which word documents are provided. (for e.g. BrandX.html). These file will be saved in 'ResultHTMLS' folder.

## Code explained

The script runs through all folders contained in 'InputDocx' folder.

define brandPerInitialLoadMap as Map<String, String>
define brandPerHeadListMap as Map<String, String>
define brandPerHtmlBodyMap as Map<String, String>

for every brand in InputDocx folder:
    put brand as key in brandPerInitialLoadMap and initial load as value
    define headListString as String 
    define htmlBodyString as String
    for every country in brand folder:
        for every docxfile in the country folder:
            define language as String, get it's value from the title of the file (method)
            
            trasform it into an html file and save it with the same naming convention as for docx file but with .html extension
