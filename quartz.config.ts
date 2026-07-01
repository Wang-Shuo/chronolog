import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "ChronoLog",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "localhost:8080",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      "_pipeline",
      "docs",
      "tests",
      "node_modules",
      "quartz",
    ],
    defaultDateType: "modified",
    theme: {
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f8f7f2",
          lightgray: "#dedbd2",
          gray: "#6c6a63",
          darkgray: "#34332f",
          dark: "#171714",
          secondary: "#9b6a19",
          tertiary: "#3f6f6b",
          highlight: "rgba(155, 106, 25, 0.15)",
          textHighlight: "#fff0bd",
        },
        darkMode: {
          light: "#171714",
          lightgray: "#34332f",
          gray: "#9d9a90",
          darkgray: "#dedbd2",
          dark: "#f8f7f2",
          secondary: "#d49a36",
          tertiary: "#74aaa4",
          highlight: "rgba(212, 154, 54, 0.2)",
          textHighlight: "#5a4314",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: false }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
