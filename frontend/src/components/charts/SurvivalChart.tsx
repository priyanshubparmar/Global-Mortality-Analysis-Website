import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  Area,
  ReferenceDot
} from "recharts";

export default function SurvivalChart({ data, currentAge }: any) {

  const currentPoint = data.find((d:any) => d.Age === currentAge);

  return (
    <div style={{ width: "100%", height: 450 }}>

      <ResponsiveContainer>

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="Age" />

          <YAxis domain={[0,1]} />

          <Tooltip />

          {/* Confidence Interval */}
          <Area
            type="monotone"
            dataKey="upper"
            stroke="none"
            fill="#90caf9"
            fillOpacity={0.25}
          />

          <Area
            type="monotone"
            dataKey="lower"
            stroke="none"
            fill="#ffffff"
          />

          {/* Survival curve */}
          <Line
            type="monotone"
            dataKey="survival_probability"
            stroke="#2563eb"
            strokeWidth={3}
            dot={false}
          />

          {/* Highlight current age */}
          {currentPoint && (
            <ReferenceDot
              x={currentPoint.Age}
              y={currentPoint.survival_probability}
              r={6}
              fill="red"
            />
          )}

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
}