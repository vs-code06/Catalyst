import ReactFlow, { Background, Controls } from "reactflow";
import "reactflow/dist/style.css";

interface DependencyGraphProps {
  repoId: string;
}

export function DependencyGraph({ repoId: _repoId }: DependencyGraphProps) {
  // Simple stub rendering react-flow
  const initialNodes = [
    { id: "1", position: { x: 100, y: 100 }, data: { label: "Main Module" } },
    { id: "2", position: { x: 300, y: 100 }, data: { label: "Parser Module" } },
  ];
  const initialEdges = [{ id: "e1-2", source: "1", target: "2" }];

  return (
    <div className="h-[600px] w-full border border-surface-border rounded-xl overflow-hidden bg-surface-secondary">
      <ReactFlow defaultNodes={initialNodes} defaultEdges={initialEdges} fitView>
        <Background color="#2a3347" gap={16} />
        <Controls className="react-flow__controls" />
      </ReactFlow>
    </div>
  );
}
export default DependencyGraph;
