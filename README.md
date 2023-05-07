# 使用流程

1. `pip install -r requirements.txt`
2. `python get_web_content.py`
   - 爬取ansible官网的文档，作为知识库语料
3. 下载spacy分词的中文分词器
   ```shell
   python -m spacy download zh_core_web_lg
   python -m spacy download zh_core_web_sm
   ```
4. 新增`.env`文件，具体格式参照`.env.template`文件，填入`OPENAI_API_KEY`
5. 运行`doc-copilot.ipynb`
   - 因为使用了 OpenAI 的 Embedding 模型, 注意运行的时候需要挂代理