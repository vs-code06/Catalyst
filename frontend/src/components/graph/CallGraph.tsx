interface CallGraphProps {
  repoId: string;
}

export function CallGraph({ repoId }: CallGraphProps) {
  return (
    <div className="flex h-[400px] w-full items-center justify-center border border-surface-border rounded-xl bg-surface-secondary text-gray-400">
      Call Graph Visualization Stub for repository: {repoId} (Cytoscape.js container)
    </div>
  );
}
export default CallGraph;
