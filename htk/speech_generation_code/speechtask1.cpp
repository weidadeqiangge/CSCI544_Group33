// speechtask1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <sapi.h>
#include <iostream>
#include<string>
std::wstring s2ws(const std::string& str);
int _tmain(int argc, _TCHAR* argv[])
{

	_TCHAR s[100];
	int spointer = 0;
	for (int i = 1; i < argc; i++)
	{
		_TCHAR *tmps = argv[i];
		int argcnt = 0;
		while(tmps[argcnt] != '\0')
		{
			s[spointer] = tmps[argcnt];
			spointer++;
			argcnt++;
		}
		//std::cout << "finishi" << std::endl;
		s[spointer++] = ' ';
	}
	if (spointer > 0)
	{
		s[spointer] = '\0';
	}
	/*std::wstring res = s;
	std::wcout << res;
	std::string sheader = "<rate speed = \"-1\">";
	std::string sendheader = "< /rate>";
	std::wstring wheader = s2ws(sheader);
	std::wstring wendheader = s2ws(sendheader);
	std::wstring realres = wheader + res + wendheader;
	std::wcout << realres;
	_TCHAR *str = new _TCHAR (realres.length()+1);
	_TCHAR *p = str;
	int i = 0;
	for ( i= 0; i < realres.length(); i++)
	{
		p[i] = realres[i];
	}
	std::cout << "finishi" << std::endl;
	p[i] = _TCHAR('\0');*/
	ISpVoice * pVoice = NULL;

	if (FAILED(::CoInitialize(NULL)))
		return FALSE;
	HRESULT hr = CoCreateInstance(CLSID_SpVoice, NULL, CLSCTX_ALL, IID_ISpVoice, (void **)&pVoice);
	if (SUCCEEDED(hr))
	{
		hr = pVoice->Speak(L"I want A tiket from hongkong to london", 0, NULL);
		pVoice->Release();
		pVoice = NULL;
	}
	
	::CoUninitialize();
//	delete[] str;
	return TRUE;
}

std::wstring s2ws(const std::string& str)
{
	int size_needed = MultiByteToWideChar(CP_UTF8, 0, &str[0], (int)str.size(), NULL, 0);
	std::wstring wstrTo(size_needed, 0);
	MultiByteToWideChar(CP_UTF8, 0, &str[0], (int)str.size(), &wstrTo[0], size_needed);
	return wstrTo;
}