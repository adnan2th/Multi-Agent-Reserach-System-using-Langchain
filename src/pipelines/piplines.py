from src.Agents.Agents import Build_Serach_Agent, Build_Scrape_Agent, Writer_chain, critic_chain    

def run_research_pipeline(topic: str) -> str:
    state = {}
    print("\n"+" ="*50)
    print("step 1 - serach agent is working ...")
    print("="*50)

    search_agent = Build_Serach_Agent()
    search_result = search_agent.invoke({
    "messages": [("human", f"Find recent  ,raliable and detailed about : {topic}")]
       })
    
    state["search_result"] = search_result["messages"][-1].content
    print("\n search result ", state["search_result"])

    print("\n"+" ="*50)
    print("step 2 - scrape agent is working ...")
    print("="*50)

    reader_agent = Build_Scrape_Agent()
    reader_agent = reader_agent.invoke(
        {
            "messages": [("user",
               f"Based on the following search results about '{topic}',"
               f"pick the most relevant URL and scrape it for deeper content.\n\n"
               f"Search Results: \n{state['search_result'][:800]}" 
             )]
        }
    )

    state['scraped_content'] = search_result["messages"][-1].content
    print("\n scraped content ", state["scraped_content"])

    print("\n"+" ="*50)
    print("step 3 - writing agent is working ...")
    print("="*50)

    research_report = (
        f"Search Results:\n{state['search_result']}\n\n"
        f"Detailed Scraped Content:\n{state['scraped_content']}"
    )

    state['report'] = Writer_chain.invoke({
        "topic": topic,
        "research": research_report
    })

    print("\n Final report ", state["report"])


    print("\n"+" ="*50)
    print("step 4 - critic agent is working ...")
    print("="*50)

    state['feedback'] = critic_chain.invoke({
        "report": state['report']})

    print("\n critic report ", state["feedback"])

    return state

    
    






