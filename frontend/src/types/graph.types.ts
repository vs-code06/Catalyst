export interface NodeData {
  label: string;
  type?: string;
  loc?: number;
  complexity?: number;
}

export interface GraphNode {
  id: string;
  data: NodeData;
  position?: { x: number; y: number };
}

export interface GraphEdge {
  id: string;
  source: string;
  target: string;
  label?: string;
  animated?: boolean;
}

export interface SoftwareGraph {
  nodes: GraphNode[];
  edges: GraphEdge[];
}
