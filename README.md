PyFarsi's PasteBin 

Features : 
- Syntax Highlighting
- Create documents with nc(Netcat)
- Api

Todo :
- Create documents in website

Api Usage :
1. For create documents : 
- Api url : /api/documents
- Request body : content (content = 'your code')
- Request method : POST
- Response Content-type : application/json

2. For get document content(You can use /raw/*key* instead of this api) : 
- Api url : /api/getdoc
- Request body : key (key = 'key of a paste')
- Request method : POST
- Response Content-type : application/json

------------------------------------------------------

Special Thanks to :
- [MagnumDingusEdu](https://github.com/MagnumDingusEdu) for [SocksBin](https://github.com/MagnumDingusEdu/SocksBin)
- [PrismJs](https://github.com/prismjs/Prism)
