export interface ExtractedSymbol {
  name: string;
  kind: "class" | "function" | "module" | "variable";
  line: number;
  filePath: string;
}

export interface ParseJob {
  jobId: string;
  status: "pending" | "running" | "success" | "failed";
  repoUrl: string;
}
