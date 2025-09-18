# reworkd/AgentGPT: 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser.

Column: https://github.com/reworkd/AgentGPT
Processed: No
created on: April 19, 2023 11:20 AM

Assemble, configure, and deploy autonomous AI Agents in your browser.

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/banner.png)

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f916.png)

[](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d6e6f6465266d6573736167653d2532302533453d31362e302e30266c6f676f3d6e6f64652e6a7326636f6c6f723d3233333444303538)

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f517.png)

[Short link](https://agentgpt.reworkd.ai/)

•

[Contribute](https://github.com/reworkd/AgentGPT#-getting-started)

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f91d.png)

•

[Twitter](https://twitter.com/asimdotshrestha/status/1644883727707959296)

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f426.png)

AgentGPT allows you to configure and deploy Autonomous AI agents. Name your own custom AI and have it embark on any goal imaginable. It will attempt to reach the goal by thinking of tasks to do, executing them, and learning from the results

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f680.png)

.

## Features

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f389.png)

This platform is currently in beta, we are currently working on:

- Long term memory
    
    ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f9e0.png)
    
- Web browsing
    
    ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f310.png)
    
- Interaction with websites and people
    
    ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f468-1f469-1f466.png)
    

More Coming soon...

## Tech Stack

- **Bootstrapping**: [create-t3-app](https://create.t3.gg/).
    
    ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/2705.png)
    
- **Framework**: [Nextjs 13 + Typescript](https://nextjs.org/).
- **Auth**: [Next-Auth.js](https://next-auth.js.org/)
- **ORM**: [Prisma](https://prisma.io/).
- **Database**: [Supabase](https://supabase.com/).
- **Styling**: [TailwindCSS + HeadlessUI](https://tailwindcss.com/).
- **Typescript Schema Validation**: [Zod](https://github.com/colinhacks/zod).
- **End-to-end typesafe API**: [tRPC](https://trpc.io/).

## Getting Started

![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f468-1f680.png)

> 
> 
> 
> ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f6a7.png)
> 
> [Nodejs +16 (LTS recommended)](https://nodejs.org/en/)
> 
1. Fork this project:
- [Click here](https://github.com/reworkd/AgentGPT/fork).
1. Clone the repository:

```
git clone git@github.com:YOU_USER/AgentGPT.git
```

1. Install dependencies:

```
npm install
```

1. Create a **.env** file with the following content:

> 
> 
> 
> [schema](https://github.com/reworkd/AgentGPT/blob/main/src/env/schema.mjs)
> 

```
# Deployment Environment:
NODE_ENV=development

# Next Auth config:
# Generate a secret with `openssl rand -base64 32`
NEXTAUTH_SECRET=changeme
NEXTAUTH_URL=http://localhost:3000

# Prisma
DATABASE_URL=file:./db.sqlite

# External APIs:
OPENAI_API_KEY=changeme
```

1. Ready , now run:
    
    ![](reworkd%20AgentGPT%20%F0%9F%A4%96%20Assemble,%20configure,%20and%20deploy%2005e465d655b14b0583662c1d45227e1a/1f973.png)
    

```
# Create database migrations
npx prisma db push

# Run the project:
npm run dev
```