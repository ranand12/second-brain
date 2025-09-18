# Tools Simon AI

Column: https://simonwillison.net/dashboard/tools/
Processed: Yes
created on: November 12, 2024 7:22 PM

All entries that link to [https://tools.simonwillison.net/](https://tools.simonwillison.net/) in some way

Owned by **simonw**, visibility: Unlisted

- SQL query
    
    ```
    with content as (
    select
        'entry' as type,
        id,
        created,
        title,
        body,
        is_draft
    from
        blog_entry
    
    union
    
    -- selecting from blog_blogmark
    select
        'blogmark' as type,
        id,
        created,
        link_title as title,
        commentary as body,
        is_draft
    from
        blog_blogmark
    
    union
    
    -- selecting from blog_quotation
    select
        'quotation' as type,
        id,
        created,
        source as title,
        quotation as body,
        is_draft
    from
        blog_quotation
    ),
    tools as (select distinct on (tool_url)
        unnest(regexp_matches(body, '(https://tools\.simonwillison\.net/[^<"\s)]+)', 'g')) as tool_url,
        'https://simonwillison.net/' || left(type, 1) || '/' || id as blog_url,
        title,
        date(created) as created
     from content where is_draft = false
    )
    select * from tools order by created desc
    ```
    

21 rows

| tool_url | blog_url | title | created |
| --- | --- | --- | --- |
| [https://tools.simonwillison.net/mdn-timelines](https://tools.simonwillison.net/mdn-timelines) | [https://simonwillison.net/b/8287](https://simonwillison.net/b/8287) | MDN Browser Support Timelines | 2024-11-11 |
| [https://tools.simonwillison.net/llm-prices](https://tools.simonwillison.net/llm-prices) | [https://simonwillison.net/e/8582](https://simonwillison.net/e/8582) | You can now run prompts against images, audio and video in your terminal using LLM | 2024-10-29 |
| [https://tools.simonwillison.net/gpt-4o-audio-player?gist=GIST_ID_HERE`](https://tools.simonwillison.net/gpt-4o-audio-player?gist=GIST_ID_HERE%60) | [https://simonwillison.net/b/8259](https://simonwillison.net/b/8259) | Prompt GPT-4o audio | 2024-10-28 |
| [https://tools.simonwillison.net/gpt-4o-audio-player?gist=4a982d3fe7ba8cb4c01e89c69a4a5335](https://tools.simonwillison.net/gpt-4o-audio-player?gist=4a982d3fe7ba8cb4c01e89c69a4a5335) | [https://simonwillison.net/b/8259](https://simonwillison.net/b/8259) | Prompt GPT-4o audio | 2024-10-28 |
| [https://tools.simonwillison.net/svg-sandbox](https://tools.simonwillison.net/svg-sandbox) | [https://simonwillison.net/b/8256](https://simonwillison.net/b/8256) | Mastodon discussion about sandboxing SVG data | 2024-10-26 |
| [https://tools.simonwillison.net/openai-audio](https://tools.simonwillison.net/openai-audio) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/sqlite-wasm](https://tools.simonwillison.net/sqlite-wasm) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/extract-urls](https://tools.simonwillison.net/extract-urls) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/qr](https://tools.simonwillison.net/qr) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/text-wrap-balance-nav](https://tools.simonwillison.net/text-wrap-balance-nav) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/clipboard-viewer](https://tools.simonwillison.net/clipboard-viewer) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/jina-reader](https://tools.simonwillison.net/jina-reader) | [https://simonwillison.net/e/8578](https://simonwillison.net/e/8578) | Everything I built with Claude Artifacts this week | 2024-10-21 |
| [https://tools.simonwillison.net/image-to-svg](https://tools.simonwillison.net/image-to-svg) | [https://simonwillison.net/b/8174](https://simonwillison.net/b/8174) | VTracer | 2024-10-07 |
| [https://tools.simonwillison.net/gemini-chat](https://tools.simonwillison.net/gemini-chat) | [https://simonwillison.net/b/8089](https://simonwillison.net/b/8089) | Gemini Chat App | 2024-08-27 |
| [https://tools.simonwillison.net/tiff-orientation](https://tools.simonwillison.net/tiff-orientation) | [https://simonwillison.net/e/8482](https://simonwillison.net/e/8482) | Building a tool showing how Gemini Pro can return bounding boxes for objects in images | 2024-08-26 |
| [https://tools.simonwillison.net/gemini-bbox](https://tools.simonwillison.net/gemini-bbox) | [https://simonwillison.net/e/8482](https://simonwillison.net/e/8482) | Building a tool showing how Gemini Pro can return bounding boxes for objects in images | 2024-08-26 |
| [https://tools.simonwillison.net/image-resize-quality](https://tools.simonwillison.net/image-resize-quality) | [https://simonwillison.net/e/8482](https://simonwillison.net/e/8482) | Building a tool showing how Gemini Pro can return bounding boxes for objects in images | 2024-08-26 |
| [https://tools.simonwillison.net/box-shadow](https://tools.simonwillison.net/box-shadow) | [https://simonwillison.net/b/7919](https://simonwillison.net/b/7919) | Box shadow CSS generator | 2024-07-08 |
| [https://tools.simonwillison.net/arena-animated](https://tools.simonwillison.net/arena-animated) | [https://simonwillison.net/e/8413](https://simonwillison.net/e/8413) | Open challenges for AI engineering | 2024-06-27 |
| [https://tools.simonwillison.net/haiku](https://tools.simonwillison.net/haiku) | [https://simonwillison.net/e/8337](https://simonwillison.net/e/8337) | AI for Data Journalism: demonstrating what we can do with this stuff right now | 2024-04-17 |
| [https://tools.simonwillison.net/ocr](https://tools.simonwillison.net/ocr) | [https://simonwillison.net/e/8334](https://simonwillison.net/e/8334) | Running OCR against PDFs and images directly in your browser | 2024-03-30 |
- Copy and export data

Duration: 175.32ms