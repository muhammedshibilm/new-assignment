"use client";
import React, { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useEffect } from "react";
import API from "@/lib/api";
import { getCurrentUser } from "@/lib/auth";

export default function RegisterPage() {
  const router = useRouter();
  const [data, setData] = useState({ name: "", email: "", password: "" });
  const [error, setError] = useState("");

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((user) => {
      if (mounted && user) {
        router.replace("/");
      }
    });

    return () => {
      mounted = false;
    };
  }, [router]);

  async function handleRegister(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    try {
      const res = await API.post("/api/auth/register", data);

      if (res.status === 201) {
        router.push("/login");
      }
    } catch (err: unknown) {
      const message =
        typeof err === "object" &&
        err !== null &&
        "response" in err &&
        typeof (err as { response?: { data?: { detail?: string } } }).response?.data
          ?.detail === "string"
          ? (err as { response?: { data?: { detail?: string } } }).response?.data
              ?.detail ?? "Registration failed"
          : "Registration failed";
      setError(message);
    }
  }

  return (
    <div className="h-screen  flex items-center justify-center ">
      <div className="space-y-2">
        <h1 className="text-3xl font-bold text-center">Register</h1>
        <form onSubmit={handleRegister} className="space-y-2">
          <input
            className="border-2 rounded-lg py-2 px-1 "
            type="text"
            placeholder="name"
            value={data.name}
            onChange={(e) => setData({ ...data, name: e.target.value })}
            required
          />
          <br />

          <input
            className="border-2 rounded-lg py-2 px-1 "
            type="email"
            placeholder="Email"
            value={data.email}
            onChange={(e) => setData({ ...data, email: e.target.value })}
            required
          />
          <br />
          <input
            className="border-2 rounded-lg py-2 px-1 "
            type="password"
            placeholder="Password"
            value={data.password}
            onChange={(e) => setData({ ...data, password: e.target.value })}
            required
          />
          <br />
          <button
            type="submit"
            className=" bg-white text-center w-full text-black  py-2 rounded-lg hover:cursor-pointer"
          >
            Register
          </button>
          <p className="text-xs text-center">
            if you have account{" "}
            <Link href={"/login"} className="text-gray-500">
              Click here
            </Link>{" "}
          </p>
          {error && <p className="text-red-500">{error}</p>}
        </form>
      </div>
    </div>
  );
}
