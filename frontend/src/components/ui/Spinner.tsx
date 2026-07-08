import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export interface SpinnerProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: "sm" | "md" | "lg";
}

export function Spinner({ className, size = "md", ...props }: SpinnerProps) {
  return (
    <div
      className={twMerge(
        clsx(
          "animate-spin rounded-full border-2 border-current border-t-transparent text-catalyst-500",
          {
            "h-4 w-4 border": size === "sm",
            "h-8 w-8 border-2": size === "md",
            "h-12 w-12 border-3": size === "lg",
          }
        ),
        className
      )}
      {...props}
    />
  );
}
