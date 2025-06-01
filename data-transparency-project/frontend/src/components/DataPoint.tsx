import React from "react";

interface Source {
  name: string;
  url: string;
}

interface DataPointProps {
  title: string;
  description?: string;
  source: Source;
}

const DataPoint: React.FC<DataPointProps> = ({ title, description, source }) => {
  return (
    <div style={{ border: "1px solid #ddd", padding: "12px", marginBottom: "8px", borderRadius: "4px" }}>
      <h4>{title}</h4>
      {description && <p>{description}</p>}
      <small>
        Source:{" "}
        <a href={source.url} target="_blank" rel="noopener noreferrer" title={source.name}>
          {source.name}
        </a>
      </small>
    </div>
  );
};

export default DataPoint;

