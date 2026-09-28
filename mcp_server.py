"""MCP stdio server for Butterworth Filter."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ButterworthFilter

filter_inst = ButterworthFilter()

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "apply_butterworth_filter",
                        "description": "Filter a discrete signal sequence using second-order Butterworth IIR low-pass",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "signal": {"type": "array", "items": {"type": "number"}},
                                "cutoff_ratio": {"type": "number", "default": 0.2}
                            },
                            "required": ["signal"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "apply_butterworth_filter":
            sig = args.get("signal", [])
            cutoff = float(args.get("cutoff_ratio", 0.2))
            bf = ButterworthFilter(cutoff)
            out = [bf.filter_sample(s) for s in sig]
            return {"jsonrpc": "2.0", "id": req_id, "result": {"filtered_signal": out}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
